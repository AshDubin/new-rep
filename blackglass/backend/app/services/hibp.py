import os
import requests


def check_email_breach(email: str):
    """Query HaveIBeenPwned for breaches of the given email."""
    api_key = os.environ.get("HIBP_API_KEY")
    if not api_key:
        return {"error": "HIBP_API_KEY not set"}

    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "blackglass-osint",
    }
    resp = requests.get(url, headers=headers, params={"truncateResponse": "false"})
    if resp.status_code == 404:
        return {"breaches": []}
    resp.raise_for_status()
    return resp.json()
