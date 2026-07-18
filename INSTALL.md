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

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Create `frontend/.env` from `frontend/.env.example` when changing the API base URL.
