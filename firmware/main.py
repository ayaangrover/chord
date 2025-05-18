import time
import wifi
import socketpool
import adafruit_requests
from spotify import SpotifyClient
from display import Display

WIFI_SSID = 'WIFI_SSID'
WIFI_PASSWORD = 'WIFI_PASSWORD'

# Spotify API credentials
CLIENT_ID = 'CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'
REFRESH_TOKEN = 'REFRESH_TOKEN'

def connect_wifi():
    print("Connecting to WiFi...")
    wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connected:", wifi.radio.ipv4_address)

def main():
    connect_wifi()

    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())

    spotify = SpotifyClient(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        refresh_token=REFRESH_TOKEN,
        requests_session=requests
    )
    
    display = Display()

    while True:
        info = spotify.get_current_playing()
        if info:
            display.show(info)
        else:
            print("Nothing is currently playing.")
        time.sleep(30)

if __name__ == '__main__':
    main()