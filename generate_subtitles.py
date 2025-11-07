import os
import whisper
from audio_extractor import extract_audio


model = whisper.load_model("base")


def generate_subtitles(vedios_path):
    
    audio_path = extract_audio(vedios_path)
    
    result = model.transcribe(audio_path)
    
    # print(result)
    
    srt_path = os.path.splitext(vedios_path)[0] + ".srt"
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for i, seg in enumerate(result["segments"], start = 1):
            start = seg["start"]
            end = seg["end"]
            text = seg["text"].strip()
            
            
            def srt_timestamp(seconds):
                millis = int((seconds - int(seconds)) * 1000)
                h, m, s = int(seconds // 3600), int((seconds % 3600) // 60), int(seconds % 60)
                
                return f"{h:02d}:{m:02d}:{s:02d},{millis:03d}"

            srt_file.write(f"{i}\n")
            srt_file.write(f"{srt_timestamp(start)} --> {srt_timestamp(end)}\n")
            srt_file.write(f"{text}\n\n")
    
    
    print(f"✅ Subtitles saved at: {srt_path}")
    
