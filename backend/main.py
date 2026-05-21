from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from config import FRONTEND_URL
from routes import match, jobs
from db import get_conn
from init_db import init_db
from services.ai_service import score_cv_job
from auth import hash_password, verify_password, create_token
from jose import jwt
import os


app = FastAPI()

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JWT_SECRET = os.getenv("JWT_SECRET")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/match")
def match(data: dict):

    try:


        cv = data.get("cv", "").lower()

        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO cv_profiles (cv_text) VALUES (%s) RETURNING id",
            (cv,)
        )
        cv_id = cursor.fetchone()[0]

        jobs = [
            {
                "title": "Python Backend Developer",
                "company": "TechCorp",
                "location": "Remote",
                "description": "python fastapi postgresql docker api"
            },
            {
                "title": "DevOps Engineer",
                "company": "CloudOps",
                "location": "EU",
                "description": "docker aws linux kubernetes"
            },
            {
                "title": "Data Engineer",
                "company": "DataWorks",
                "location": "Remote",
                "description": "python sql postgresql api"
            }
        ]
        

        matches = []

        for job in jobs:

            result = score_cv_job(cv, job["description"])

            cursor.execute("""
                INSERT INTO job_matches
                (cv_id, job_title, score, strengths, missing_skills)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                cv_id,
                job["title"],
                result["score"],
                ",".join(result["strengths"]),
                ",".join(result["missing_skills"])
            ))


            matches.append({
                "title": job["title"],
                "company": job["company"],
                "location": job["location"],
                "score": min(result["score"], 100),
                "strengths": result["strengths"],
                "missing_skills": result["missing_skills"]
            })

        conn.commit()
        cursor.close()
        conn.close()

        matches.sort(key=lambda x: x["score"], reverse=True)

        return {"matches": matches}
    
    except Exception as e:
        return {"error": str(e)}

@app.post("/register")
def register(data: dict):

    conn = get_conn()
    cursor = conn.cursor()

    try:
        email = data["email"]
        password = hash_password(data["password"])

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )
        conn.commit()

        return {"status": "registered"}
    
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()


@app.post("/login")
def login(data: dict):

    conn = get_conn()
    cursor = conn.cursor()

    try: 
        cursor.execute(
            "SELECT password FROM users WHERE email=%s",
            (data["email"],)
        )

        row = cursor.fetchone()

        if not row:
            return {"error": "User not found"}
    
        if not verify_password(data["password"], row[0]):
            return{"error": "Wrong password"}
    
        token = create_token(data["email"])

        return {"token": token}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()

@app.get("/history")
def history(token: str):

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=["HS256"]
        )
        email = payload["sub"]

        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT jm.job_title, jm.score
            FROM job_matches jm
            JOIN cv_profiles cp ON jm.cv_id = cp.id
            ORDER BY jm.id DESC
            LIMIT 20
        """)
        rows = cursor.fetchall()

    

        cursor.close()
        conn.close()

        return {
            "email": email,
            "history": [
                {
                    "job": r[0],
                    "score": r[1]
                }
                for r in rows
            ]
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/report")
def report(token: str):

    payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=["HS256"]
    )

    email = payload["sub"]

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT job_title, score
        FROM job_matches
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    filename = "report.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"AI Resume Report - {email}",
            styles["Title"]
        )
    )

    for r in rows:
        content.append(
            Paragraph(
                f"{r[0]} - {r[1]}%",
                styles["Normal"]
            )
        )
    
    doc.build(content)

    cursor.close()
    conn.close()

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename="resume_report.pdf"
    )

    