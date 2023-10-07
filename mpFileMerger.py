from moviepy.editor import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Load the MP4 video
video_clip = VideoFileClip("Data/Cosmic Reef [1280 X 720].mp4")

# Load the MP3 audio
audio_clip = AudioFileClip("output_music.wav")

# Set the audio of the video to the loaded MP3 audio
video_clip = video_clip.set_audio(audio_clip)

# Write the result to a new MP4 file
video_clip.write_videofile("Data/output_video.mp4", codec="libx264")