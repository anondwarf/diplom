def generate_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"{token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }