import requests
import json

def auto_like(post_url, session):
    like_url = post_url + "/like/"
    response = session.post(like_url)
    
    if response.status_code == 200:
        return "✅ Liked the post!"
    else:
        return "❌ Failed to like"

if __name__ == "__main__":
    session = requests.Session()
    print(auto_like("https://www.instagram.com/p/example_post", session))
