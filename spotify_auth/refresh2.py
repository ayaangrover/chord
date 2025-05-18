import base64
import requests

client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
code = 'REFRESH_CODE'  # Replace with the actual code you received from the refresh1.py script, then test this script. make sure you fill out both CLIENT_ID and CLIENT_SECRET with your actual Spotify app credentials as well
redirect_uri = 'http://127.0.0.1:8080/callback'

auth_str = f"{client_id}:{client_secret}"
b64_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Authorization": f"Basic {b64_auth}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri
}

response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

print(response.json())