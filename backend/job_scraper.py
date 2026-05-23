import requests
from bs4 import BeautifulSoup

def fetch_jobs():

    url = "https://nofluffjobs.com/pl/jobs/backend"

    html = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    ).text

    soup = BeautifulSoup(
        html,
        "html.parser"
    )
    
    jobs = []

    cards = soup.find_all("a")[:20]

    for c in cards:

        title = c.get_text(strip=True)

        if len(title) > 10:

            jobs.append({
                "title": title,
                "company": "NoFluffJobs",
                "location": "Remote",
                "description": title
            })
    return jobs