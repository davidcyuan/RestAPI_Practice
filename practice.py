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
    print()
  


# ── Pattern 2: GET a specific resource by ID ──────────────────────────────────
# Write get_post(post_id) that:
#   - Makes a GET request to /posts/{post_id}
#   - Prints the status code
#   - Prints the post's id, title, and body
def get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    print("Status code:", response.status_code)
    print("Post ID:", response.json().get("id"))
    print("Post Title:", response.json().get("title"))
    print("Post Body:", response.json().get("body"))
    print()


# ── Pattern 3: POST a new resource ────────────────────────────────────────────
# Write create_post(title, body, user_id) that:
#   - Makes a POST request to /posts with a JSON payload
#   - Prints the status code (JSONPlaceholder returns 201 Created)
#   - Prints the full response including the new id
#
# Hint: requests.post(url, json={...}) — use json= not data= for JSON APIs
def create_post(title, body, user_id):
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    print()


# ── Pattern 4: Parse JSON and extract specific fields ─────────────────────────
# Write get_user_info(user_id) that:
#   - Makes a GET request to /users/{user_id}
#   - Extracts and prints: name, email, and city (nested under address.city)
#
# Hint: the response is a nested dict — access nested fields with chained []
def get_user_info(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    user_data = response.json()
    print("Name:", user_data.get("name"))
    print("Email:", user_data.get("email"))
    print("City:", user_data.get("address", {}).get("city"))
    print()


# ── Pattern 5: Handle errors (non-200 status codes) ───────────────────────────
# Write safe_get_post(post_id) that:
#   - Makes a GET request to /posts/{post_id}
#   - If status is 200, prints the title
#   - If status is 404, prints a "not found" message
#   - For anything else, prints the status code and raises an exception
#
# Hint: response.raise_for_status() or check response.status_code manually
# Test it: JSONPlaceholder returns 404 for IDs > 100
def safe_get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if(post_id == 67):
        response.status_code = 500
    if response.status_code == 200:
        print("Title:", response.json().get("title"))
    elif response.status_code == 404:
        print(f"Post with ID {post_id} not found.")
    else:
        print("Unexpected status code:", response.status_code)
        response.raise_for_status()
    


# get_all_posts()
# get_post(1)
# create_post("My New Post", "This is the body of my new post.", 1)
# get_user_info(1)
safe_get_post(1)
safe_get_post(67)  # Should trigger 404 handling