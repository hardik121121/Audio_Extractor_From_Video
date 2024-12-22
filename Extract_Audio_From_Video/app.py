# pip install moviepy

import moviepy as mp

# Load the video file
cvt_video = mp.VideoFileClip("Video.3gp")

# Extract the audio from the video
ext_audio = cvt_video.audio

# Write the audio to an mp3 file
ext_audio.write_audiofile("audio_Extracted.mp3")
