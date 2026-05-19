from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import FRONTEND_URL
from routes import match, jobs


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(match.router)
app.include_router(jobs.router)



@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/match")
def match(data: dict):

    cv = data.get("cv", "")

    jobs = [
        {
            "title": "Python Backend Developer",
            "company": "TechCorp",
            "location": "Remote",
            "description": "Python FastAPI PostgreSQL REST API Docker"
        },
        {
            "title": "DevOps Engineer",
            "company": "CloudOps",
            "location": "EU",
            "description": "Docker AWS Linux Kubernetes"
        },
        {
            "title": "Data Engineer",
            "company": "DataWorks",
            "location": "Remote",
            "description": "Python SQL PostgreSQL API"
        }
        
    ]

    results = []

    for job in jobs:
        result = score_cv_job(cv, job["description"])

        results.append({
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "score": result["score"],
            "strengths": result["strengths"],
            "missing_skills": result["missing_skills"]

        })
    
    results.sort(key=lambda x: x["score"], reverse=True)

    
    return {"matches": results}

