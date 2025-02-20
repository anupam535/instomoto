import requests

def create_instagram_account(email, otp):
    try:
        print(f"[INFO] Creating Instagram account with Email: {email} and OTP: {otp}")
        
        # Simulated Instagram registration request (Replace with real API)
        instagram_api_url = "https://www.instagram.com/accounts/web_create_ajax/"
        headers = {"User-Agent": "Mozilla/5.0"}
        data = {
            "email": email,
            "otp": otp,
            "username": "random_username",  # Modify as needed
            "password": "random_password123",  # Modify as needed
        }

        response = requests.post(instagram_api_url, headers=headers, data=data)

        if response.status_code == 200:
            return f"Instagram Account Created! ✅ Email: {email}"
        else:
            return None

    except Exception as e:
        print("[ERROR] Instagram account creation failed:", e)
        return None
