import subprocess
from pathlib import Path


name_of_output = "PDVideo.mp4"
file_to_convert = "C:/Users/USER/Videos/PD.MOV"
video_path = Path(file_to_convert)
complete_file = video_path.parent/name_of_output

ffmpeg_list = [

    "ffmpeg",

    "-i", file_to_convert,

    "-vf", "scale=-2:720",

    "-pix_fmt", "yuv420p",

    "-c:v", "libx264",

    "-crf", "28",

    "-preset", "veryfast",

    "-c:a", "aac",

    "-b:a", "128k",

    complete_file

]

subprocess.Popen(ffmpeg_list)