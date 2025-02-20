import json

def load_proxies():
    try:
        with open("data/proxies.json", "r") as f:
            proxies = json.load(f)
        return proxies
    except FileNotFoundError:
        return []

def get_random_proxy():
    proxies = load_proxies()
    if proxies:
        return proxies[0]  # Change this to randomly select a proxy
    return None

if __name__ == "__main__":
    print(get_random_proxy())
