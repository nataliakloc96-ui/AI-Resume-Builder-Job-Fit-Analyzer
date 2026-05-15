def score_cv_job(cv: str, job_desc: str):
    cv = cv.lower()
    job_desc = job_desc.lower()

    keywords = ["python", "fastapi", "sql", "docker", "api", "aws"]

    score = 0 
    strengths = []
    missing = []

    for k in keywords:
        if k in cv and k in job_desc:
            score += 10
            strenghts.append(k)
        elif k in job_desc and k not in cv:
            missing.append(k)
    
    return {
        "score": min(score, 100),
        "strengths": strengths,
        "missing": missing
    }
