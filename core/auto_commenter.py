import requests
import random

comments_list = ["🔥🔥🔥", "Awesome post!", "Great content!", "Keep it up!", "Amazing!"]

def auto_comment(post_url, session):
    comment_text = random.choice(comments_list)
    comment_url = post_url + "/comment/"
    
    payload = {"comment_text": comment_text}
    response = session.post(comment_url, data=payload)
    
    if response.status_code == 200:
        return f"✅ Commented: {comment_text}"
    else:
        return "❌ Failed to comment"

if __name__ == "__main__":
    session = requests.Session()
    print(auto_comment("https://www.instagram.com/p/example_post", session))
