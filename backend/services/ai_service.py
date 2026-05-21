def score_cv_job(cv: str, job_desc: str):
    
    
    cv = cv.lower()
    job_desc = job_desc.lower()

    keywords = ["python", "fastapi", "sql", "docker", "api", "aws", "postgresql", "linux"]

    
    strengths = []
    missing_skills = []

    for k in keywords:
        if k in cv and k in job_desc:
            score += 12
            strengths.append(k)
        elif k in job_desc and k not in cv:
            missing.append(k)
    
    score = int(
        len(strengths) /
        max(1, len(strengths) + len(missing_skills)) * 100
    )
    
    return {
        "score": score,
        "strengths": strengths,
        "missing_skills": missing_skills
    }
