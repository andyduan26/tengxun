# Install

## Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Health check:

```bash
curl http://127.0.0.1:8000/api/health/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser account to manage video projects, categories, VIP status, image URLs, sort weights, and CSV exports.

## Deployment

Recommended deployment uses Vercel for the frontend and Railway for the backend.
Legacy Netlify and Render configuration files are kept for compatibility.

Frontend deployment uses `vercel.json`. Import the GitHub repository in Vercel
with the project root left as the repository root, then configure this
environment variable:

```text
VITE_API_BASE_URL=https://<your-railway-backend-domain>/api
```

Backend deployment uses `railway.json`. Configure these environment variables
in Railway:

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=<strong-random-secret>
DJANGO_ALLOWED_HOSTS=<your-backend-domain>
CORS_ALLOWED_ORIGINS=<your-frontend-origin>
CSRF_TRUSTED_ORIGINS=<your-frontend-origin>,<your-backend-origin>
DATABASE_URL=<railway-postgresql-url>
```

Railway supplies `RAILWAY_PUBLIC_DOMAIN` automatically after a public domain is
generated, and `railway.json` binds Gunicorn to Railway's `$PORT`.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Create `frontend/.env` from `frontend/.env.example` when changing the API base URL.
