from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=LXWKNN0lPsQ')
for i in yt.streams.filter(progressive=True, file_extension='mp4', type="video").order_by('resolution').desc():
    print(i)