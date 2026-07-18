# Install

## Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:5000
```

Health check:

```bash
curl http://127.0.0.1:5000/api/health/
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Create `frontend/.env` from `frontend/.env.example` when changing the API base URL.
