# Project Initialization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first runnable Vue3 + Django/DRF project foundation.

**Architecture:** Use one repository with `backend/` and `frontend/` roots. Django owns REST APIs under `/api/`; Vue consumes those APIs through an Axios client configured by `VITE_API_BASE_URL`.

**Tech Stack:** Django LTS, Django REST Framework, django-cors-headers, django-simpleui, Vue3, Vite, Vue Router, Pinia, Axios, TailwindCSS.

## Global Constraints

- Follow AGENTS.md fixed stack: Vue3 + Vite frontend and Django + DRF backend.
- Keep this stage limited to initialization and health-check connectivity.
- Every stage must remain runnable.
- Maintain README.md, CHANGELOG.md, API.md, and INSTALL.md.

---

### Task 1: Backend Foundation

**Files:**
- Create: `backend/manage.py`
- Create: `backend/config/settings.py`
- Create: `backend/config/urls.py`
- Create: `backend/config/asgi.py`
- Create: `backend/config/wsgi.py`
- Create: `backend/apps/core/views.py`
- Create: `backend/apps/core/urls.py`
- Create: `backend/apps/core/tests.py`
- Create: `backend/requirements.txt`
- Create: `backend/.env.example`

**Interfaces:**
- Produces: `GET /api/health/` returning `{"success": true, "data": {"status": "ok", "service": "backend"}, "message": "Backend is healthy"}`

- [x] **Step 1: Create Django project files**
- [x] **Step 2: Add health API test**
- [x] **Step 3: Add minimal DRF API implementation**
- [x] **Step 4: Run `python manage.py check` and `python manage.py test`**

### Task 2: Frontend Foundation

**Files:**
- Create: `frontend/package.json`
- Create: `frontend/index.html`
- Create: `frontend/vite.config.js`
- Create: `frontend/tailwind.config.js`
- Create: `frontend/postcss.config.js`
- Create: `frontend/src/main.js`
- Create: `frontend/src/App.vue`
- Create: `frontend/src/router/index.js`
- Create: `frontend/src/stores/app.js`
- Create: `frontend/src/api/client.js`
- Create: `frontend/src/views/HomeView.vue`
- Create: `frontend/src/assets/main.css`
- Create: `frontend/.env.example`

**Interfaces:**
- Consumes: `VITE_API_BASE_URL`
- Produces: Vue app that builds with `npm run build`

- [x] **Step 1: Create Vite Vue files**
- [x] **Step 2: Add router, Pinia, Axios, and base styling**
- [x] **Step 3: Run `npm run build`**

### Task 3: Documentation And Commit

**Files:**
- Create: `README.md`
- Create: `CHANGELOG.md`
- Create: `API.md`
- Create: `INSTALL.md`
- Create: `.gitignore`

**Interfaces:**
- Produces: project initialization documentation for local development.

- [x] **Step 1: Document setup and API**
- [x] **Step 2: Commit with `feat: initialize vue django project`**
