import os
import numpy as np 
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
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

    return response.data[0].embedding

def cosine(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )

def score_cv_job(cv, job_desc):

    cv_vec = embedding(cv)
    job_vec = embedding(job_desc)

    similarity = cosine(
        cv_vec,
        job_vec
    )

    score = int(similarity * 100)

    if score < 0:
        score = 0
    
    if score > 100:
        score = 100
    
    strengths = []

    if score > 80:
        strengths.append(
            "Strong semantic fit"
        )
    
    elif score > 60:
        strengths.append(
            "Moderate semantic fit"
        )
    
    missing_skills = []

    return {
        "score": score,
        "strengths": strengths,
        "missing_skills": missing_skills
    }



