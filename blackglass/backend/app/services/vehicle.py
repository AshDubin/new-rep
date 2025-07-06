import requests

MOT_URL = "https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests?registration={plate}"
# Placeholder for API key or service integration

def lookup_plate(plate: str):
    # Example call to UK government MOT API (not functional without key)
    headers = {"Accept": "application/json"}
    resp = requests.get(MOT_URL.format(plate=plate), headers=headers)
    if resp.status_code == 404:
        return None
    if resp.status_code >= 400:
        resp.raise_for_status()
    return resp.json()
