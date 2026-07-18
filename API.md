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

## Home Banners

### `GET /api/home/banners/`

Returns the latest 5 video projects for the homepage carousel, ordered by `sort_weight`, `created_at`, and `id`.

## Home Recommendations

### `GET /api/home/recommendations/?category=全部`

Returns video project cards for the homepage recommendation section.

Query params:

- `category`: `全部`, `电视剧`, `电影`, `动漫`, `综艺`, `纪录片`, `短剧`

Example:

```bash
curl "http://127.0.0.1:8000/api/home/recommendations/?category=电视剧"
```

## MongoDB JSON Reference

The active backend uses Django models per project rules. If this data is imported into MongoDB later, the equivalent JSON shape is:

```json
[
  {
    "title": "仙逆",
    "description": "青宜：只此一次，却真香！",
    "coverImageUrl": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1800&q=85",
    "thumbnailUrl": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=900&q=85",
    "category": "动漫",
    "isVip": true,
    "sortWeight": 100
  },
  {
    "title": "脱口秀3",
    "description": "爆笑回归，金句不断，笑到停不下来。",
    "coverImageUrl": "https://images.unsplash.com/photo-1527224538127-2104bb71c51b?auto=format&fit=crop&w=1800&q=85",
    "thumbnailUrl": "https://images.unsplash.com/photo-1527224538127-2104bb71c51b?auto=format&fit=crop&w=900&q=85",
    "category": "综艺",
    "isVip": false,
    "sortWeight": 90
  }
]
```
