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


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/match")
def match(data: dict):

    cv = data.get("cv", "").lower()

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

        score = 0
        strengths = []
        missing = []

        for skill in job["description"].split():

            if skill in cv:
                score += 20
                strengths.append(skill)
            else:
                missing.append(skill)

        matches.append({
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "score": min(score, 100),
            "strengths": strengths,
            "missing_skills": missing
        })

    matches.sort(key=lambda x: x["score"], reverse=True)

    return {"matches": matches}