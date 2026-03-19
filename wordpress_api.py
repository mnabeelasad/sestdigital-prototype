# wordpress_api.py
import os
import requests
from requests.auth import HTTPBasicAuth

def post_draft_to_wordpress(title, content, category):
    """
    Publishes the generated article as a draft to a WordPress site using the REST API.
    Requires WP_URL, WP_USER, and WP_APP_PASSWORD in the .env file.
    """
    wp_url = os.getenv("WP_URL")
    wp_user = os.getenv("WP_USER")
    wp_password = os.getenv("WP_APP_PASSWORD")

    # If the user hasn't set up a personal WP demo, we return a successful mock response
    if not wp_url or not wp_user or not wp_password:
        return {
            "status": "mock_success",
            "message": "Demo Mode: WordPress credentials not found in .env. If keys were provided, this would be published as a draft."
        }

    # The actual API Call logic
    api_endpoint = f"{wp_url}/wp-json/wp/v2/posts"
    
    # Map the text category to a generic WP category ID (usually 1 is 'Uncategorized')
    category_mapping = {"Strategy": 2, "Training": 3, "Technology": 4}
    cat_id = category_mapping.get(category, 1)

    payload = {
        "title": title,
        "content": content,
        "status": "draft",
        "categories": [cat_id]
    }

    try:
        response = requests.post(
            api_endpoint,
            auth=HTTPBasicAuth(wp_user, wp_password),
            json=payload
        )
        if response.status_code == 201:
            return {"status": "success", "url": response.json().get("link")}
        else:
            return {"status": "error", "message": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}