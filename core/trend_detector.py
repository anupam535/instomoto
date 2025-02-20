import requests

def detect_trending_hashtags():
    trending_api = "https://www.instagram.com/explore/tags/"
    response = requests.get(trending_api)
    
    if response.status_code == 200:
        trends = response.json()
        return f"🔥 Trending Hashtags: {trends}"
    else:
        return "❌ Failed to fetch trending hashtags"

if __name__ == "__main__":
    print(detect_trending_hashtags())
