# Tencent Video Clone

Enterprise-grade full-stack video website project initialized with Vue3 and Django REST Framework.

## Stack

- Frontend: Vue3, Vite, Vue Router, Pinia, Axios, TailwindCSS
- Backend: Django, Django REST Framework, django-cors-headers, SimpleUI
- Development database: SQLite
- Production database target: PostgreSQL

## Current Stage

Stage 1 initializes the project foundation and provides a backend health check endpoint.

## Quick Start

See `INSTALL.md` for local setup steps.

## Deployment

- Frontend: Vercel, configured by `vercel.json`
- Backend: Railway, configured by `railway.json`
- Frontend API base URL: `VITE_API_BASE_URL=https://<backend-domain>/api`
