import requests
import base64
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser

CLIENT_ID = 'CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'
REDIRECT_URI = 'http://127.0.0.1:8080/callback' # you can put anything here, but it must match the one registered in your Spotify dev portal(the trailing / matters!)
SCOPES = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': SCOPES,
})
print("Opening browser for Spotify authorization...")
webbrowser.open(auth_url)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code = self.path.split("code=")[-1]
        print("Authorization code received.")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'You can close this window.')
        token_url = 'https://accounts.spotify.com/api/token'
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        r = requests.post(token_url, headers=headers, data=data)
        print("Token response:")
        print(r.json())

httpd = HTTPServer(('localhost', 8888), Handler)
httpd.handle_request()