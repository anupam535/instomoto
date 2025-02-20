import requests
import json

def auto_follow(user_id, session):
    follow_url = f"https://www.instagram.com/web/friendships/{user_id}/follow/"
    
    response = session.post(follow_url)
    
    if response.status_code == 200:
        return f"✅ Followed User ID: {user_id}"
    else:
        return "❌ Failed to Follow"

if __name__ == "__main__":
    session = requests.Session()
    print(auto_follow("example_user_id", session))
