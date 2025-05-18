# Chord: A Spotify Car Thing Replacement.

#### Chord is a spotify carthing replacement(without the controls). It's powered by a Seeed Studio Xiao ESP32S3 and the display is Seeed Studio's "Round Display for Seeed Studio XIAO". It fetches the song name, artist, and cover via the spotify developer api with the Xiao ESP32S3's 2.4ghz wifi, which is very convienient seeing as the xiao itself is only $7.99.(more about that in the BOM below). You can also get instructions to compile the code for it below, and enjoy! (Note: the software might not work yet, i don't have the microcontroller to test it on. I'll write more when i've tested and possibly fixed it.)

## BOM:

Note: BOM is also available at bom.csv.

| Component| Quantity | Description | Price | Purpose |
|-------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------|
| **Seeed Studio XIAO ESP32S3** | 1        | Wi-Fi microcontroller, runs the firmware                                                                                                                        | $23.85 (incl. tax/shipping) | backbone of the project - uses micropython to run the code
| **Seeed Studio Round Display**| 1        | 1.28" 240x240 GC9A01 TFT display with touch. Shipping/tax included above (bought with XIAO)                                                                     | $19.99                  | display to show the time/music info based on whether something is currently playing
| **LiPo Battery (3.7V, 2200mAh)** | 1     | Optional, for wireless use; plugs directly into the XIAO battery connector. From [Adafruit](https://www.adafruit.com/product/2011)                                   | $26.03 (incl. tax/shipping) | For wireless use/travel/storage/power outages
| **Flat Right Angle USB-C Cable**   | 1        | [Flatter cable](https://www.amazon.com/Extension-Charging-66W%EF%BC%88Not-compatible-100W-240W/dp/B0CSW5W4LY) for top-mounted port                             | $9.99                   | For charging, needed to get the cable from the top of the device to the bottom without being too obvious or fat.
| **Charging Cable**            | 1        | [Fast braided cable](https://www.amazon.com/Anker-Bio-Braided-Charger-iPhone15-15ProMax/dp/B0BHQH89ZQ) for flashing and/or powering the device                 | $14.99                  | To power the device really fast (and flash the firmware)
| **3D Printed Case**           | 1        |  STL available in `/case`; printed via JLCPCB | $24.80 ($1.80 print + $23 shipping) | To protect the hardware and keep it in place

**Total: $119.65**

## Firmware Setup and Flashing:

First, go to /spotify_auth/README.md and follow the instructions. Then, go to /firmware/README.md and follow the instructions.

## Case:

The case is a modified version of the suggested stl from Seeed Studio for their display that fits a battery as well. Use the modified stl from `/case` if you are adding a battery.

You can see a render at /images/case.png