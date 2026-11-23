# ScholarFind — Project P26 | Roll No. 26

Educational scholarship finder with synthetic scholarship data. **Not an official scholarship eligibility service.**

## Quick start
```bash
python -m pip install -r requirements.txt
python src/app.py
```
Open http://localhost:5000. Run tests with `python -m pytest tests -q`.

## Features
- Search three demonstration scholarship records through API.
- Check marks, annual income, and category using deterministic rules.
- Generate document checklist and explain reasons for eligibility results.
- Basic health endpoint; GitHub Actions, Docker and Jenkins configuration included.

## API
- `GET /api/scholarships`
- `POST /api/match`: `{"min_marks":85,"max_income":200000,"category":"General"}`
- `GET /health`

## Limitations
No official data feed, login, application submission, real LLM integration, officer confirmation workflow, or live monitoring dashboard. CI and Jenkins configurations are supplied but remote runs are not verified. No external service screenshots are fabricated.

## Screenshots needed
Add real screenshots in `evidence/phase1` through `phase5`: UI, Jira backlog/sprints, GitHub commits and Actions run, Jenkins pipeline, Docker container, Selenium execution, SonarQube scan and testing dashboard. Report includes a detailed evidence checklist.
