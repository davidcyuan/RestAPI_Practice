# REST API Practice

Practice making REST API calls in Python using the `requests` library against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a free fake REST API.

## Endpoints used

| Method | Path | Description |
|--------|------|-------------|
| GET | `/posts` | List of posts |
| GET | `/posts/{id}` | Single post by ID |
| POST | `/posts` | Create a post (simulated) |
| GET | `/users/{id}` | User data (for JSON parsing practice) |

## Patterns covered

1. GET a list of resources
2. GET a specific resource by ID
3. POST a new resource
4. Parse JSON responses and extract specific fields
5. Handle errors (non-200 status codes)

## Setup

```bash
pip install requests
python3 practice.py
```
