
import youtube_dl

# 定義YouTube影片的網址
video_url = "https://www.youtube.com/watch?v=GT4CuxufSxQ"

# 下載影片
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': 'video.mp4',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])



'''
編寫中
'''