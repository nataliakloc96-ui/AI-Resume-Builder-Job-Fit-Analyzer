from fastapi import APIRouter
from services.ai_service import score_cv_job

router = APIRouter()

@router.post("/match")
def match(data: dict):

    cv = data.get("cv", "")
    jobs = data.get("jobs", [])

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
    
    return {"matches": results}