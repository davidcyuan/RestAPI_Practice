import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# ── Pattern 1: GET a list of resources ────────────────────────────────────────
# Write get_all_posts() that:
#   - Makes a GET request to /posts
#   - Prints the status code
#   - Prints how many posts came back (it's a list)
#   - Prints the title of the first post
#
# Hint: requests.get(url), response.status_code, response.json()
# Optional: filter by user with params={"userId": 1}

def get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print("Status code:", response.status_code)
    posts = response.json()
    print("Number of posts:", len(posts))
    if posts:
        print("Title of first post:", posts[0]["title"])
  


# ── Pattern 2: GET a specific resource by ID ──────────────────────────────────
# Write get_post(post_id) that:
#   - Makes a GET request to /posts/{post_id}
#   - Prints the status code
#   - Prints the post's id, title, and body
def get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    print("Status code:", response.status_code)
    


# ── Pattern 3: POST a new resource ────────────────────────────────────────────
# Write create_post(title, body, user_id) that:
#   - Makes a POST request to /posts with a JSON payload
#   - Prints the status code (JSONPlaceholder returns 201 Created)
#   - Prints the full response including the new id
#
# Hint: requests.post(url, json={...}) — use json= not data= for JSON APIs


# ── Pattern 4: Parse JSON and extract specific fields ─────────────────────────
# Write get_user_info(user_id) that:
#   - Makes a GET request to /users/{user_id}
#   - Extracts and prints: name, email, and city (nested under address.city)
#
# Hint: the response is a nested dict — access nested fields with chained []


# ── Pattern 5: Handle errors (non-200 status codes) ───────────────────────────
# Write safe_get_post(post_id) that:
#   - Makes a GET request to /posts/{post_id}
#   - If status is 200, prints the title
#   - If status is 404, prints a "not found" message
#   - For anything else, prints the status code and raises an exception
#
# Hint: response.raise_for_status() or check response.status_code manually
# Test it: JSONPlaceholder returns 404 for IDs > 100


get_all_posts()