import board
import displayio
import busio
import gc9a01
import terminalio
import adafruit_imageload
import time
import framebufferio
import rgbmatrix
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import adafruit_requests as requests
import io
import supervisor
import vectorio
import gc
import ssl
import socketpool
from wifi import radio

class Display:
    def __init__(self):
        displayio.release_displays()

        spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)

        tft_cs = board.D1
        tft_dc = board.D3
        tft_reset = None 

        display_bus = displayio.FourWire(
            spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset
        )

        self.display = gc9a01.GC9A01(
            display_bus, width=240, height=240, rotation=0
        )

        self.main_group = displayio.Group()
        self.display.show(self.main_group)

        self.image_group = displayio.Group()
        self.main_group.append(self.image_group)

        self.overlay_bitmap = displayio.Bitmap(240, 60, 1)
        self.overlay_palette = displayio.Palette(1)
        self.overlay_palette[0] = 0x000000 

        self.overlay_sprite = displayio.TileGrid(
            self.overlay_bitmap, pixel_shader=self.overlay_palette, x=0, y=180
        )
        self.overlay_sprite.alpha = 128 
        self.main_group.append(self.overlay_sprite)

        self.song_label = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=10, y=190)
        self.artist_label = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=10, y=215)
        self.time_label = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=10, y=240)

        self.main_group.append(self.song_label)
        self.main_group.append(self.artist_label)
        self.main_group.append(self.time_label)

    def show(self, info):
        while len(self.image_group) > 0:
            self.image_group.pop()

        if info is None or not info.get('is_playing', False):
            self.song_label.text = ""
            self.artist_label.text = ""
            current_time = time.localtime()
            time_str = "{:02d}:{:02d}:{:02d}".format(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
            self.time_label.text = f"Time: {time_str}"
            return

        self.song_label.text = f"Song: {info.get('song', '')}"
        self.artist_label.text = f"Artist: {info.get('artist', '')}"
        played = info.get('played', '')
        total = info.get('total', '')
        self.time_label.text = f"{played} / {total}"

        image_url = info.get('image_url', None)
        if not image_url:
            return

        try:
            pool = socketpool.SocketPool(radio)
            ssl_context = ssl.create_default_context()
            requests_session = requests.Session(pool, ssl_context)

            response = requests_session.get(image_url)
            image_bytes = response.content
            response.close()

            image_file = io.BytesIO(image_bytes)
            image, palette = adafruit_imageload.load(image_file, bitmap=displayio.Bitmap, palette=displayio.Palette)
            image_tilegrid = displayio.TileGrid(image, pixel_shader=palette, x=0, y=0)
            self.image_group.append(image_tilegrid)

        except Exception:
            while len(self.image_group) > 0:
                self.image_group.pop()
            self.song_label.text = ""
            self.artist_label.text = ""
            current_time = time.localtime()
            time_str = "{:02d}:{:02d}:{:02d}".format(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
            self.time_label.text = f"Time: {time_str}"