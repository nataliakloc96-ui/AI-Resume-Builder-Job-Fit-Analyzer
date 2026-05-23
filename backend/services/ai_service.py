import math

def tokenize(text):
    return set(
        text.lower().split()
    )

def cosine(a,b):

    common = len(a & b)
    if common == 0:
        return 0
    
    return common / math.sqrt(
        len(a) * len(b)
    )
    

def score_cv_job(cv: str, job_desc: str):
    
    
    cv = cv.lower()
    job_desc = job_desc.lower()

    keywords = ["python", "fastapi", "sql", "docker", "api", "aws", "postgresql", "linux"]

    
    strengths = []
    missing_skills = []

    for k in keywords:
        if k in cv and k in job_desc:
            strengths.append(k)
        elif k in job_desc and k not in cv:
            missing_skills.append(k)
    
    score = int(
        len(strengths) /
        max(1, len(strengths) + len(missing_skills)) * 100
    )
    
    return {
        "score": score,
        "strengths": strengths,
        "missing_skills": missing_skills
    }


def embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )


def score_cv_job(cv, job_desc):

    cv_tokens = tokenize(cv)
    job_tokens = tokenize(job_desc)

    similarity = cosine(
        cv_tokens,
        job_tokens
    )

    score = int(similarity * 100)

    strengths = []

    if score < 0:
        score = 0
    
    if score > 100:
        score = 100
    
    strengths = []

    if score > 80:
        strengths.append(
            "Strong semantic fit"
        )
    
    elif score > 50:
        strengths.append(
            "Moderate alignment"
        )
    
    else: 
        strengths.append(
            "Weak alignment"
        )
    
    missing_skills = []

    return {
        "score": score,
        "strengths": strengths,
        "missing_skills": missing_skills
    }



