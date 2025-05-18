import time
import json
import base64
import adafruit_requests

class SpotifyClient:
    def __init__(self, client_id, client_secret, refresh_token, requests_session):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.requests = requests_session
        self.access_token = None
        self.token_expiration = 0

    def _encode_credentials(self):
        creds = f"{self.client_id}:{self.client_secret}"
        return base64.b64encode(creds.encode()).decode()

    def _refresh_access_token(self):
        print("Refreshing access token...")
        headers = {
            "Authorization": f"Basic {self._encode_credentials()}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = "grant_type=refresh_token&refresh_token=" + self.refresh_token
        response = self.requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens["access_token"]
            self.token_expiration = time.monotonic() + tokens.get("expires_in", 3600)
            print("Access token refreshed.")
        else:
            print("Failed to refresh token:", response.status_code)
            print(response.text)

    def _ensure_token_valid(self):
        if not self.access_token or time.monotonic() >= self.token_expiration:
            self._refresh_access_token()

    def get_current_playing(self):
        self._ensure_token_valid()
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)

        if response.status_code == 200 and response.content:
            data = response.json()
            if data.get("item"):
                return {
                    "name": data["item"]["name"],
                    "artist": data["item"]["artists"][0]["name"],
                    "is_playing": data["is_playing"],
                    "image_url": data["item"]["album"]["images"][0]["url"],
                    "duration_ms": data["item"]["duration_ms"],
                    "progress_ms": data["progress_ms"]
                }
        else:
            print("Error fetching song:", response.status_code)
            print(response.text)
        return None