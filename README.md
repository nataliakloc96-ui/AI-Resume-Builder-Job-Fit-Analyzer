# AI Resume Builder + Job Fit Analyzer

Production-ready AI-powered SaaS platform that analyzes resumes against live backend job offers, scores candidate-job fit, generates reports, and provides analytics dashboards.

## Live Demo

Frontend (Vercel):  
ai-resume-builder-job-fit-analyzer-jade.vercel.app

Backend API (Render):  
https://ai-resume-builder-job-fit-analyzer.onrender.com

---

## Features

### AI Resume Analysis
- Resume/job fit scoring
- Semantic-style matching engine
- Strength & missing skill analysis

### Live Job Scraping
Scrapes real backend job listings from No Fluff Jobs and matches them against uploaded resumes.

### Authentication
- User registration
- Secure login
- JWT authentication

### Dashboard Analytics
- Resume analysis history
- Score tracking
- Interactive charts

### PDF Report Export
Generate downloadable PDF reports with analysis results.

### SaaS Monetization
- Free plan usage limits
- Upgrade flow via Stripe Checkout
- Pro account payment integration

### Cloud Deployment
Fully deployed production app:
- Frontend on Vercel
- Backend on Render
- PostgreSQL database

---

## Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- JWT Authentication
- ReportLab
- Stripe API
- BeautifulSoup
- Requests

### Frontend
- HTML
- JavaScript
- Chart.js

### Deployment
- Vercel
- Render

---

## Architecture

Frontend  
↓  
FastAPI API  
↓  
Authentication Layer  
↓  
Resume Scoring Engine  
↓  
PostgreSQL Storage  
↓  
Analytics + PDF + Payments

---

## API Endpoints

### Auth
`POST /register`

`POST /login`

### Resume Analysis
`POST /match`

### Reports
`GET /report`

### User History
`GET /history`

### Payments
`GET /create-checkout`

### Admin Analytics
`GET /admin`

---

## Example Workflow

1. Register account
2. Login
3. Paste resume
4. Analyze fit against live backend jobs
5. Review score dashboard
6. Export PDF report
7. Upgrade to Pro via Stripe

---

## Screenshots

Add screenshots here:

- Login page
- Resume analyzer
- Dashboard analytics
- Stripe checkout
- PDF report export

---

## Installation

Clone repo:

```bash
git clone https://github.com/nataliakloc96-ui/AI-Resume-Builder-Job-Fit-Analyzer.git
cd repo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn main:app --reload
```

Open frontend:

```bash
index.html
```

---

## Environment Variables

Create `.env`

```env
DATABASE_URL=
JWT_SECRET=
STRIPE_SECRET_KEY=
OPENAI_API_KEY=
```

---

## Business Value

This platform helps candidates instantly evaluate resume-job fit against real market opportunities, identify missing skills, and improve application targeting.

---

## Future Improvements

- True embedding-based semantic ranking
- Subscription billing
- Admin RBAC
- Background scraping jobs
- Multi-board aggregation
- Resume improvement suggestions

---

## Author

Natalia Kurek

Backend / AI / SaaS Engineering Portfolio Project
