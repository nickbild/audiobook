# PageParrot

**Details coming soon!**

PageParrot turns any book into an audiobook in seconds.

![](https://raw.githubusercontent.com/nickbild/audiobook/refs/heads/main/media/logo_sm.jpg)

## How It Works

PageParrot is powered by a Raspberry Pi Zero 2 W single-board computer and a USB webcam. It runs a [Python script](https://github.com/nickbild/audiobook/blob/main/read_page.py) that waits for a button press, then snaps a picture of the book with the webcam. The image is then sent to Google’s Gemini 2.5 Flash large language model, along with a prompt instructing it to tell me all the text contained in the image. The text it returns is then fed into Piper to synthesize speech, which is played on a Bluetooth speaker.

## Media

![](https://raw.githubusercontent.com/nickbild/audiobook/refs/heads/main/media/hardware_close_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/audiobook/refs/heads/main/media/reader_angled_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/audiobook/refs/heads/main/media/reader_front_16-9_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/audiobook/refs/heads/main/media/reader_straight_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/audiobook/refs/heads/main/media/reader_top_sm.jpg)

## Bill of Materials

- 1 x Raspberry Pi Zero 2 W
- 1 x USB webcam
- 1 x Bluetooth speaker
- 1 x Push button
- Aluminum extrusions, wire, twist ties, and hot glue

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
