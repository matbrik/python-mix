import youtube_dl

options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': '%(title)s.%(ext)s',     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])



"""
better solution found

"""