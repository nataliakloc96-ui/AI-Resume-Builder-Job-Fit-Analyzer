from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import FRONTEND_URL
from routes import match, jobs


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-resume-builder-job-fit-analyzer-jade.vercel.app"
    ],
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
def match():
    return {"ok": True}

