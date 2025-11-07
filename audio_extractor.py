import os
import subprocess

def extract_audio(video_path, audio_path="audio.wav"):
    """Extract audio from video using ffmpeg"""
    command = [
        "ffmpeg", "-i", video_path,
        "-vn", "-acodec", "pcm_s16le",
        "-ar", "16000", "-ac", "1", audio_path, "-y"
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Extraction of the audio is completed")
    return audio_path