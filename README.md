# viddownloader

## What is this? 

If in short, personal mini-project that utilizes [yt-dlp](https://github.com/yt-dlp/yt-dlp) library to download videos or audio from YouTube. 

## DISCLAIMER

THIS PROJECT IS DECREPIT, I am making new one on C, which will cover all the TODO stuff.

Almost all of the code was copied over from examples of yt-dlp, I just put it togther so all you need is to give a link.
I am not proud of myself. 

## Why not just use yt-dlp library right away? 

Because I am an idiot. Also, I wanted to make it really simple and convinient for me to use. All of this project was a mistake, probably.

## How do you use it

### Installation

Copy directory, use `pip3 install -r requirements.txt`.

### Video

You will need to use `python3 main.py -v <link to the video>`. This will download video in mp4 format. 

### Audio

Use `python3 main.py -a <link to the video>`. This will download audio in m4a format.

## Dependencies

    * yt-dlp
    * ffmpeg
