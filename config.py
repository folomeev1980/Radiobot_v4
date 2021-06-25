import os
import re
import time
import converter
from pytube import YouTube

help = "Привет Это RadioBot, для скачивания mp3 c youtube:\n\n\
Пожалуйста, введите ссылку на видео, вида:  https:.......... ?"


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
            "audio_bitrate": 48,
            "audio_frequency": "44100",
            "audio_codec": "MP3",
            "audio_qscale": -1,

        },
        "file": open(filename, 'rb')
    })
    process.wait()

    process.download('output.mp3')


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
