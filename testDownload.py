import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=1WbS2P_dxOM",
                    proxies={"https": "https://10.104.1.9:8080"})


video = yt.streams[0]
video.download(filename='C://Users//folomeev//Videos//Captures//win11')
