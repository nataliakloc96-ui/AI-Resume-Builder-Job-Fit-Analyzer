from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text:str):
    return model.encode(text)[0]


def score_cv_job(cv: str, job: str):
    cv_vec = embed(cv)
    job_vec = embed(job)

    score = cosine_similarity([cv_vec], [job_vec])[0][0]

    return round(float(score) * 100, 2)