import yt_dlp
import sys

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

    ydl_opts = { 
    'format': 'bestvideo/best/mp4',

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
            print("\t-v for downloading video --> UNDER CONSTRACTION")
            print("\t-a for downloading only audio in m4a format")
            print("This piece of code is only held together by hopes and yt-dlp library")
            print("GitHub: https://github.com/yt-dlp/yt-dlp")
        if(f[1] == "-a"):
            downloadAudio(f[2])
        if(f[1] == "-v"):
            downloadVideo(f[2])

    except Exception as e: 
        print(f"Something went wrong: {e.args[0]}")
        

# print(URL)

options(sys.argv)


"""
potential uses of ffmpeg
    FFmpegConcatPP,
    FFmpegCopyStreamPP,
    FFmpegEmbedSubtitlePP,
    FFmpegExtractAudioPP,
    FFmpegFixupDuplicateMoovPP,
    FFmpegFixupDurationPP,
    FFmpegFixupM3u8PP,
    FFmpegFixupM4aPP,
    FFmpegFixupStretchedPP,
    FFmpegFixupTimestampPP,
    FFmpegMergerPP,
    FFmpegMetadataPP,
    FFmpegPostProcessor,
    FFmpegSplitChaptersPP,
    FFmpegSubtitlesConvertorPP,
    FFmpegThumbnailsConvertorPP,
    FFmpegVideoConvertorPP,
    FFmpegVideoRemuxerPP,
"""