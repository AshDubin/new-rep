import requests

GITHUB_URL = "https://api.github.com/users/{username}"
REDDIT_URL = "https://www.reddit.com/user/{username}/about.json"
INSTAGRAM_URL = "https://www.instagram.com/{username}/?__a=1&__d=dis"


def github_profile(username: str):
    resp = requests.get(GITHUB_URL.format(username=username))
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def reddit_profile(username: str):
    headers = {"User-Agent": "blackglass-osint"}
    resp = requests.get(REDDIT_URL.format(username=username), headers=headers)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def instagram_profile(username: str):
    resp = requests.get(INSTAGRAM_URL.format(username=username))
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()
