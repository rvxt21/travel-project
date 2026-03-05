import requests


def validate_place_via_artic_api(place_name: str) -> int | None:
    """
    Searches the Art Institute API by name and returns the external_id
    if a valid match is found.
    """
    url = f"https://api.artic.edu/api/v1/places/search"
    params = {"q": place_name, "limit": 1}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data.get("data"):
            return None

        place_id = data["data"][0]["id"]
        return int(place_id)

    except requests.RequestException:
        return None
