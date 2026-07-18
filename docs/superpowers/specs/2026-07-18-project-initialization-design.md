# Project Initialization Design

## Goal

Create a stable first-stage full-stack foundation for a Tencent Video-style website while following the project AGENTS.md stack: Vue3 + Vite + Vue Router + Pinia + Axios on the frontend, Django LTS + Django REST Framework on the backend, SQLite for development, and PostgreSQL-ready settings for production.

## Architecture

The repository uses a single Git project with two isolated application roots: `frontend/` for the Vue application and `backend/` for the Django API. The frontend reads `VITE_API_BASE_URL` and calls the backend through Axios. The backend exposes RESTful JSON under `/api/` and starts with a health endpoint to prove connectivity.

## Stage 1 Scope

Stage 1 creates only a runnable shell:

- Django project configuration under `backend/config/`
- Core app under `backend/apps/core/`
- Health check API at `GET /api/health/`
- Vite Vue app under `frontend/`
- Router, Pinia, Axios client, and a minimal premium-style home view
- Project documentation files required by AGENTS.md

## Out of Scope

Tencent Video homepage content, media models, authentication, admin business models, uploads, search, recommendations, and deployment are intentionally deferred to later stages.

## Verification

Stage 1 is complete only when these commands pass:

- `python manage.py check`
- `python manage.py test`
- `npm run build`
