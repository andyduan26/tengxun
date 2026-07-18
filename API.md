# API

## Response Format

```json
{
  "success": true,
  "data": {},
  "message": "OK"
}
```

## Health Check

### `GET /api/health/`

Returns backend availability status.

Response:

```json
{
  "success": true,
  "data": {
    "status": "ok",
    "service": "backend"
  },
  "message": "Backend is healthy"
}
```
