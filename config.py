import os
import re
import time
import converter
from youtube_dl import YoutubeDL
from pytube import YouTube
import cloudconvert

help = "Привет Это RadioBot, для скачивания mp3 c youtube:\n\n\
Пожалуйста, введите ссылку на видео, вида:  https:.......... ?"




def get_title(video):

    with YoutubeDL() as ydl:
          info_dict = ydl.extract_info(video, download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None)
    return (video_title)



def convert_low32(filename):
    time.sleep(15)

    try:
        os.remove('output.mp3')
    except FileNotFoundError:
        pass

    time.sleep(15)
    api = converter.Api('yW5eTpoFJKgINxd7wpdeBdlsl1T5OyWlQ9xMrGyVkRJbxRwHWKpJYNQuz36P7KPY')
    process = api.convert({
        "inputformat": "webm",
        "outputformat": "mp3",
        "input": "upload",
        "converteroptions": {
            "audio_bitrate": 40,
            "audio_frequency": "44100",
            "audio_codec": "MP3",
            "audio_qscale": -1,

        },
        "file": open(filename, 'rb')
    })
    process.wait()

    process.download('output.mp3')


def converter_api2():
    time.sleep(15)

    try:
        os.remove('output.mp3')
    except FileNotFoundError:
        pass

    time.sleep(15)
    cloudconvert.configure(
        api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZjdiYThiYjUyMGY0MjBkMTY5YzZjODFjNjIzMzk0NDU1ZThjNzBmMjVjNDk4Y2JjZDM3ZTZjNGFmMWI4YTk3NTQ5ZTdiYTMwN2ZhYTZjMTMiLCJpYXQiOjE2NDEyNDIxNTIuNDk2MzQ5LCJuYmYiOjE2NDEyNDIxNTIuNDk2MzUyLCJleHAiOjQ3OTY5MTU3NTIuNDg3NTksInN1YiI6IjMzODM2NTg5Iiwic2NvcGVzIjpbInByZXNldC5yZWFkIiwicHJlc2V0LndyaXRlIiwid2ViaG9vay53cml0ZSIsIndlYmhvb2sucmVhZCIsInRhc2sud3JpdGUiLCJ0YXNrLnJlYWQiLCJ1c2VyLndyaXRlIiwidXNlci5yZWFkIl19.IFx60SJBtEYwXJ7XskKzgO6Y0WgTJ5ZAhGj3HR60fqWm3rQWy71SGp2kcyRhJxCVSll1K4O9z9-pSAqiR9nZXYktk08G3ETmTNdvBpP1MtUBfR4fL5PIJuDEYZFYODmNS_hdkgHDWAA5xkXqPzJ2XIoV5Jp1rlmTRiKJqo3gadii6wvPlMB0Yof-nVDSfsgxcCxqW2kLECUs0PWejk3q5Q96gEk812FWIevyeYmk8rjLub-nAbtYcYRG_uR6Nk56bf7pgFYMDjGHajnl7lj4bsNK8yEJZlL9tHHAfTPoTGdkdBMChAGI4xUZ_0EALtVIaDuIdcLuq1asY8X4I_Irk6Oak1Jd-jAP056tSjgiEGAxCUPNWFKJYjoSsA_llYLx6o4yvW-96J1w5WtSFAKT5YOZ8I7C2COD7bhjwtsh_mf-8Ps4igJGRoVp5-Dx_GNiGdM0Yy2ZLWx1m9loOqCqHXzINYFRFXrS4PU9wo7WCFNWMydDgd3mgUk8JqH1RfrSLmwDrv8R3Mki5zCbi5qjZSiKgALzFhT9HS2dTkb94JK9GWReyJrGw3hC7Jwq-kJ7s_uU_-Vdv9uT_A8e5zGKpIJFZU952fTldhDsRclRgTr49JOJQOZ-oQ9Rirn9uwkMzz1U-zR0j7Z3vMC6J-O0EvsOmseEzACjfKMrRXGXbq8',
        sandbox=False)

    job = cloudconvert.Job.create(payload={
        "tasks": {
            'import-my-file': {
                'operation': 'import/upload',
                # 'url': 'https://my-url'
            },
            'convert-my-file': {
                'operation': 'convert',
                "input_format": "webm",
                "output_format": "mp3",
                'some_other_option': 'value',
                "input": ['import-my-file'],
                "audio_bitrate": 40
            },
            'export-my-file': {
                'operation': 'export/url',
                'input': 'convert-my-file'
            }
        }
    })

    upload_task_id = job['tasks'][0]['id']
    convert_task_id = job['tasks'][1]['id']
    export_task_id = job['tasks'][2]['id']

    upload_task = cloudconvert.Task.find(id=upload_task_id)
    cloudconvert.Task.upload(file_name='input.webm', task=upload_task)

    exported_url_task_id = export_task_id
    res = cloudconvert.Task.wait(id=exported_url_task_id)  # Wait for job completion
    file = res.get("result").get("files")[0]
    # res = cloudconvert.download(filename=file['filename'], url=file['url'])
    res = cloudconvert.download(filename='output.mp3', url=file['url'])



def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


# Получение YOUTUBE_ID

def youtube_link(message_text):
    if len(message_text) == 28:
        youtube_id = re.search('\w\/(.*)', message_text).group(1)
    elif (message_text) == 57:
        youtube_id = re.search('/watch...(.*).feature', message_text).group(1)
    else:
        youtube_id = re.search('/watch...(...........)', message_text).group(1)

    mp3_link = 'https://www.youtube.com/watch?v=' + youtube_id

    return mp3_link


def remove_files():
    if os.path.exists('input.webm'):
        os.remove('input.webm')

    if os.path.exists('input.mp4'):
        os.remove('input.mp4')

    if os.path.exists('output.mp3'):
        os.remove('output.mp3')

    else:
        print('Нет файлов для удаления')


if __name__ == '__main__':
    pass
