from cvision import Vision, RealTime
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download():
    global video

    url = "url"
    
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    
    ys = yt.streams.get_highest_resolution()
    ys.download()

    video = yt.title + '.mp4'

download()

v = Vision(video)
v.detect_persons()

#rt = RealTime()
#rt.run()