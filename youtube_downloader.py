from pytube import YouTube

if __name__ == '__main__':
    yt = YouTube ("https://www.youtube.com/watch?v=9I59xl7U37g")
    stream = yt.streams.get_highest_resolution()
    stream.download()
