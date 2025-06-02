---
title: "Chord"
author: "Ayaan Grover(@ayaangrover)"
description: "A spotify carthing replacement for my desk!"
created_at: "2025-05-20"
---


## Total 19 hrs + 1hrs writing the journal logs

## May 15, 2025 - 8 hours - did a ton of research and a bunch of planning

Saw the Highway info today. It looked awesome, so I spent a long time planning and researching for my first project. Here was my thought process today.

1) I've always loved spotify's carthing and I saw a video on youtube once about using it at your desk. However, that was after it was discontinued, and now it's hard to find one for under $100 on ebay, even open box and used.
2) I've tried to make my own, but my raspberry pi tiny display i got isn't small enough - it's 7-8 inches which is huge compared to what I want. Using Highway, I can get a new screen that's smaller and actually realistic in terms of size and weight.

I now have to name it! I asked chatgpt(obviously, where else would i go for random names) and i eventually got it to spit out "chord". I thought that sounded good so i made my gh repo. Then i did more research.

I found some good options quite soon - notably [this](https://www.waveshare.com/2.8inch-dpi-lcd.htm) one. However, i didn't think that a full rpi was my best option, and that screen was too bulky. I also found [this](https://www.adafruit.com/product/5393) but the exposed pins would mean a large bezel(which i hate).

Ironically, my final decision actually included a fairly large bezel, but i'm happy with it because 1) its round and 2) its touchscreen. While i don't plan on using the touchscreen yet as this will be a display and not a controller, it's going to be good if i ever add controls.

Unfortunately I only realised I didn't like the older display after making something in kicad(which turned out to be useless since the xiao literally just plugs into the display). Oh well.

In the end, I settled on [this](https://www.seeedstudio.com/Seeed-Studio-Round-Display-for-XIAO-p-5638.html) round one. To be fair, this was only because it has built in connections for the xiao [esp32s3](https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32S3-Pre-Soldered-p-6334.html), and that's really convenient, especially since it's usb c and tiny!

Do I regret not choosing [this 1.69 inch rounded color lcd](https://www.seeedstudio.com/1-69inch-240-280-Resolution-IPS-LCD-Display-Module-p-5755.html) instead, since it has no exposed pins? Yeah. But i kinda like the fully round display which looks like a fake nest thermostat.

## May 16, 2025 - 1.5 hours - did some research and wiring!

I just did a bunch of research on the docs of the xiao and display. Then i made a wiring diagram(in figma ofc lol). I also asked gpt to help me make sure i wasnt missing any parts for the project. i have a small list now, and i think im ready to do the code tomorrow!

## May 17, 2025 - 9.5 hours - Finished project!

Wow I did so much work today. I finished the whole project(i know, im already done!!!). Took a long time - a bit of thinking, a lot of doing stuff.

1) Did a bunch of research on spotify api. i've used it before but not too much, so I had to research exactly how i'd do this. I also asked gpt for its opinion on minimizing the amount of buttons the user has to click on Chord. that took abt 2 hrs but i figured everything out eventually. oh yeah also i'm using micropython because i don't know c++.
2) I made the first bit of the code. So the way it works(if im not mistaken) is there's a `CLIENT_ID`, a `CLIENT_SECRET`, a `REFRESH_TOKEN`, and an `ACCESS_TOKEN`. The Client ID and Client Secret are obtained when you set up the project in spotify dev dashboard. Using some code gpt helped me understand and make, we figured out how to generate a refresh token and access token(it's in refresh1.py under /spotify_auth). however, the access_token only lasts an hour. for that reason, the xiao needs to regenerate an access token every hour so that it can fetch the data like song name and album cover and artist and more. we did a test(refresh2.py under /spotify_auth) and successfully made the access token(after a first failure because of a redirect URI mismatch - aparrently a trailing / matters).

Finally, after 1 hr of debugging and pain, i started the rest of the code! this took a lot of research but i eventually made `main.py`, `display.py`, and `spotify.py`. the first one does the wifi and controlling. display does the showing stuff like the image and black overlay for the text at the bottom. i hope it looks good. i havent tested it yet because i don't have the xiao or display so i asked gpt and it said it looks alright(but theres some stuff i can do to make it more battery efficient). I'll be using it plugged in most of the time so no need for that. 

After about 7 hrs I finished all the firmware and research(for the firmware, not total unfortunately)!!

So then i was making a case when i saw the screen page already had a case design so i downloaded and modified it(my update is in `/case/case.stl`) to fit a battery underneath. i hope it isnt too tall now. but that took a while because i had to move the usb port cutout to be next to the display. 

## Jun 2, 2025 - 0.2 hrs - decreased overall price!

I did some research and lowered the price from $120 to $55. Used a coupon code suggested by @lordbagel42 that saves me $5 on Seeed Studio!

then i was finally done, and i exported it and started the readme. that took a while because i did so much research on pricing and stuff after shipping and then case materials. i chose treated black resin because it looks good in all the images i see online.

Now I'm here, writing this summary of today's progress. I can finally say I'm done and ready to submit. Thanks for taking the time to read/skim these 936 words!
