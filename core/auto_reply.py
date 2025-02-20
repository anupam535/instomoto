import requests
import json

# AI Model for Smart Replies
def generate_reply(message_text):
    predefined_replies = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "help": "Sure! What do you need help with?",
    }
    
    message_text = message_text.lower()
    return predefined_replies.get(message_text, "Sorry, I don't understand that.")

def auto_reply(message, session):
    reply_text = generate_reply(message)
    reply_url = "https://www.instagram.com/direct/messages/"
    
    payload = {"message_text": reply_text}
    response = session.post(reply_url, data=payload)
    
    if response.status_code == 200:
        return f"✅ Auto Replied: {reply_text}"
    else:
        return "❌ Failed to Reply"

if __name__ == "__main__":
    session = requests.Session()
    print(auto_reply("Hi", session))
