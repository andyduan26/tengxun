#!/usr/bin/env sh
set -eu

python manage.py migrate --noinput
python manage.py loaddata apps/video/fixtures/production_video_projects.json

exec gunicorn config.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
