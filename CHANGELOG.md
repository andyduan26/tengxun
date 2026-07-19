# Changelog

## 2026-07-18

- Initialized frontend and backend project structure.
- Added Django REST Framework health check API.
- Added Vue3 Vite application shell.
- Added setup and API documentation.

## 2026-07-19

- Added `VideoProject` data model for homepage video content.
- Added homepage banners and recommendations API endpoints.
- Added initial video project fixture data.
- Improved Chinese SimpleUI admin for managing video projects.
- Added dedicated `video.VideoProject` model and admin for detailed Tencent Video-style content management.
- Added optional video file upload field to video project admin.
- Prepared Django backend for Render deployment with dynamic host trust and port binding.
- Added Vercel frontend and Railway backend deployment configuration.
- Fixed Railway monorepo deployment commands for backend root directory builds.
- Forced Railway Nixpacks Python detection for backend subdirectory deployment.
- Moved Railway build and start commands into Nixpacks configuration with explicit pip support.
