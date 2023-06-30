from moviepy.editor import VideoFileClip

import os

input_video_path = "towa.mp3"

folder = "towa"

if not os.path.exists(folder):
    os.makedirs(folder)

video_clip = VideoFileClip(input_video_path)

total_sec = video_clip.duration

spilt_sec = 5

for i, start in enumerate(range(0, int(total_sec), spilt_sec)):
    end = min(start + spilt_sec, total_sec)
    segment = video_clip.subclip(start, end)

    '''
    save segment(every 5 sec)
    '''

    out_path = os.path.join(folder, f"0000{i}.wav")
    segment.audio.write_audiofile(out_path, codec="pcm_s16le", fps=44100)

video_clip.reader.close()
