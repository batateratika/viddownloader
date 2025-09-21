import yt_dlp
import sys
import os
import ffmpeg

def downloadAudio(URL):
    # Yes, this is an example code from yt-dlp
    ydl_opts = { 
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{ 
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URL)

def downloadVideo(URL):

    def format_selector(ctx):
    
        # formats are already sorted worst to best
        formats = ctx.get('formats')[::-1]

        # acodec='none' means there is no audio
        best_video = next(f for f in formats
                          if f['vcodec'] != 'none' and f['acodec'] == 'none')

        # find compatible audio extension
        audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
        # vcodec='none' means there is no video
        best_audio = next(f for f in formats if (
            f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

        # These are the minimum required fields for a merged format
        yield {
            'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
            'ext': best_video['ext'],
            'requested_formats': [best_video, best_audio],
            # Must be + separated list of protocols
            'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
        }


    ydl_opts = {
        'format': format_selector,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URL)

def options(f: str):
    try:
        if (len(f) < 2):
            raise Exception("No option has been choosen. Please run it through console and give it options. Run \"python3 main.py -h\" for help")
        if ("-" not in f[1]):
            raise Exception("No argument has been given")
        if (f[1] == "-h"):
            print("The shiitiest version of video/audio downloader for YouTube")
            print("\tmain.py [options] <link to youtube>")
            print("\t-h for help/displaying this message, doesn't require args")
            print("\t-v for downloading video in mp4 format")
            print("\t-a for downloading only audio in m4a format")
            print("This piece of code is only held together by hopes and yt-dlp library")
            print("GitHub: https://github.com/yt-dlp/yt-dlp")
        if(f[1] == "-a"):
            downloadAudio(f[2])
        if(f[1] == "-v"):
            downloadVideo(f[2])

    except Exception as e: 
        print(f"Something went wrong: {e.args[0]}")
        
options(sys.argv)
