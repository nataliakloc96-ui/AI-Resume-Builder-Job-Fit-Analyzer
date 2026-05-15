from fastapi import APIRouter
from db import get_conn

router = APIRouter()

@router.get("/jobs")
def get_jobs():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(" SELECT title, company, location FROM jobs ORDER BY id DESC LIMIT 50")
    rows = cursor.fetchall()

    conn.close()

    return (
        "jobs": [
            {"title": r[0], "company": r[1], "location": r[2]}
            for r in rows
        ]
    )
