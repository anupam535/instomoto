import requests
import json

def create_instagram_account():
    # Generate temp email
    temp_mail_api = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    try:
        response = requests.get(temp_mail_api)
        if response.status_code == 200:
            email_data = response.json()
            if email_data:
                return email_data[0]  # First generated email
            else:
                raise ValueError("Empty email response received.")
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")

    except Exception as e:
        print("Error fetching temp mail:", e)
        return None
    
    # Create Instagram Account
    insta_signup_url = "https://www.instagram.com/accounts/web_create_ajax/"
    payload = {
        "email": email,
        "username": "generated_username",
        "password": "generated_password"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(insta_signup_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        with open("data/accounts.json", "a") as f:
            json.dump({"email": email, "username": "generated_username", "password": "generated_password"}, f)
        return f"✅ Account Created: {email}"
    else:
        return "❌ Failed to create account"

if __name__ == "__main__":
    print(create_instagram_account())
