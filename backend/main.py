from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import ai import score_cv_job
import pdfplumber

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_methods=["*"],
    allow_headers=["*"],
)

JOBS = [
    {
        "title": "Python Backend Developer",
        "company": "TechCorp",
        "location": "Remote",
        "description": "Python FastAPI PostgreSQL Docker REST APIs"
    },
    {
        "title": "Data Engineer",
        "company": "DataWorks",
        "location": "EU",
        "description": "Python ETL SQL Airflow Big Data pipelines"
    },
    {
        "title": "DevOps Engineer",
        "company": "CloudOps",
        "location": "Remote",
        "description": "Docker Kubernetes AWS CI/CD Linux"
    }
    
]

def hybrid_score(cv, job):
    semantic = score_cv_job(cv, job["description"])

    keyword_bonus = 0
    keywords = ["python", "fastapi", "sql", "docker"]

    for k in keywords:
        if k in cv.lower() and k in job["description"].lower():
            keyword_bonus += 3
    
    final_score = semantic + keyword_bonus

    return min(final_score, 100)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Job Matcher API!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.get("/metrics")
def metrics():
    return {
        "total_cvs": 123,
        "total_jobs": len(JOBS),
        "average_score": 75.5
    }



@app.post("/match")
def match(payload: dict):
    try:
        cv = payload.get("cv", "")

        results = []

        for job i JOBS:
            score = score_cv_job(cv, job["description"])

            results.append({
                **job,
                "score": score,
                "reason": "Semantic similarity between CV and job description"
            })
    
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        return {"matches": results}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/cv")
def save_cv(payload: dict):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cvs (user_id, content) VALUES (%s, %s)",
        (payload["user_id"], payload["cv"])
    )

    conn.commit()
    conn.close()

    return {"status": "saved"}

@app.get("/dashboard/{user_id}")
def dashboard(user_id: int):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT jobs.title, matches.score
        FROM matches
        JOIN jobs ON jobs.id = matches.job_id
        WHERE matches.user_id = %s
    """, (user_id,))
    
    rows = cursor.fetchall()

    return {
        "matches": [
            {"title": r[0], "score": r[1]}
            for r in rows
        ]
    }

@app.post("/upload_cv")
def upload(file: UploadFile):
    with pdfplumber.open(file.file) as pdf:
        text = "/n".join(page.extract_text() for page in pdf.pages)

    return {"text": text}
