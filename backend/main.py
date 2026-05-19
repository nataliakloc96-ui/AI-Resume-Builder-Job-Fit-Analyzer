from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import FRONTEND_URL
from routes import match, jobs
from db import get_conn
from init_db import init_db
from services.ai_service import score_cv_job


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/match")
def match(data: dict):

    cv = data.get("cv", "").lower()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO cv_profiles (cv_text) VALUES (%s) RETURNING id",
        (cv,)
    )
    cv_id = cur.fetchone()[0]

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
            "score": min(score, 100),
            "strengths": strengths,
            "missing_skills": missing
        })

    conn.commit()
    cursor.close()
    conn.close()

    matches.sort(key=lambda x: x["score"], reverse=True)

    return {"matches": matches}