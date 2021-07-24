import requests
import socket

def _execute_request(
    url,
    method=None,
    headers=None,
    data=None,
    timeout=socket._GLOBAL_DEFAULT_TIMEOUT
):
    video_url = url[url.find('watch?v=') + 8:url.find('watch?v=') + 19]
    base_headers = {
        "POST": "/youtubei/v1/player HTTP/1.1",
        "Host": "www.youtube.com",
        "X-Goog-Api-Key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
    }
    data = {"context":{"client":{"clientName":"ANDROID","clientVersion":"16.05"}},
    "videoId":video_url}
    return requests.post(url="https://www.youtube.com/youtubei/v1/player", headers=base_headers, json = data).text

with open("source2.html", encoding='utf-8', mode='w') as f:
    f.write(_execute_request(url="https://www.youtube.com/watch?v=Z1wsRUTMAPI"))