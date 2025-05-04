import yt_dlp
import sys

URL = []

def options(f: str):
    try:
        if (len(f) < 2):
            raise Exception("No option has been choosen")
        if ("-" not in f[1]):
            raise Exception("No argument has been given")
        if (f[1] == "-h"):
            print("The shiitiest version of video/audio downloader for YouTube")
            print("\tmain.py [options] <link to youtube>")
            print("\t-h for help/displaying this message, doesn't require args")
            print("\t-v for downloading video ===> UNDER CONSTRUCTION")
            print("\t-a for downloading only audio in mp3 format")
            print("This piece of code is only held together by hopes and yt-dlp library")
            print("GitHub: https://github.com/yt-dlp/yt-dlp")

    

    except Exception as e: 
        print(f"Something went wrong: {e.args[0]}")
        


# print(URL)

options(sys.argv)


"""
ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URL)
"""