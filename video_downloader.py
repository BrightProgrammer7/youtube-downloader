from pytube import YouTube
from pytube import streams


video_link = input('Enter video link : ')

video = YouTube(video_link)
video.streams.get_highest_resolution().download("C:/Users/cleve/Videos/Youtube")

def finish():
    print("Download Done")

video.register_on_complete_callback(finish())