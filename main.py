from pytube import YouTube
import os


def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total - remains) / total * 100
    print(f'下載中… {percent:05.2f}', end='\r')

seed = str(input("請輸入網址: "))
yt = YouTube(seed, on_progress_callback=onProgress)

print("============================內部細項================================")
print("標題:", yt.title)
print("影片長度", yt.length)
print("影片作者", yt.author)
print("頻道網址", yt.channel_url)
print("縮圖網址", yt.thumbnail_url)
print("觀看數", yt.views)
print("===================================================================")

rename = str(input("請輸入檔案名稱: "))

# 下載影片至mp4檔案

print("download..")
yt.streams.filter().get_highest_resolution().download(filename=rename + ".mp4")
print("ok!")

# 下載影片至mp3檔案

print("download..")
yt.streams.filter().get_audio_only().download(filename=rename + ".mp3")
print("ok!")
