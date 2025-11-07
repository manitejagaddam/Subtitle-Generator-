import streamlit as st
import whisper
import tempfile
import os
from audio_extractor import extract_audio

# --- Streamlit UI ---
st.set_page_config(page_title="Subtitle Generator", page_icon="🎬", layout="centered")

st.title("🎬 Subtitle Generator using Whisper")
st.write("Upload a video, choose model accuracy, and auto-generate subtitles in `.srt` format!")

# Model selection
model_choice = st.selectbox(
    "Select Whisper Model (accuracy vs speed):",
    ["tiny", "base", "small", "medium", "large"],
    index=1
)

uploaded_video = st.file_uploader("📤 Upload your video file", type=["mp4", "mkv", "avi", "mov"])

if uploaded_video:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_video.read())
        video_path = temp_video.name

    st.video(video_path)
    st.info("Video uploaded successfully ✅")

    if st.button("Generate Subtitles 🪄"):
        st.write("Loading Whisper model... this may take a few seconds ⏳")
        model = whisper.load_model(model_choice)

        # Extract audio
        st.write("Extracting audio from video...")
        audio_path = extract_audio(video_path)

        # Transcribe
        st.write("Transcribing audio... please wait 🔊")
        result = model.transcribe(audio_path)

        # Generate .srt file
        srt_path = os.path.splitext(video_path)[0] + ".srt"
        subtitles_text = ""

        def srt_timestamp(seconds):
            millis = int((seconds - int(seconds)) * 1000)
            h, m, s = int(seconds // 3600), int((seconds % 3600) // 60), int(seconds % 60)
            return f"{h:02d}:{m:02d}:{s:02d},{millis:03d}"

        with open(srt_path, "w", encoding="utf-8") as srt_file:
            for i, seg in enumerate(result["segments"], start=1):
                start, end, text = seg["start"], seg["end"], seg["text"].strip()
                srt_line = f"{i}\n{srt_timestamp(start)} --> {srt_timestamp(end)}\n{text}\n\n"
                srt_file.write(srt_line)
                subtitles_text += srt_line

        st.success("✅ Subtitles generated successfully!")

        # --- Display Subtitles Preview ---
        st.subheader("📝 Generated Subtitles Preview")
        st.text_area("Subtitle Output", subtitles_text, height=400)

        # Provide download link
        with open(srt_path, "rb") as f:
            st.download_button(
                label="📥 Download Subtitles (.srt)",
                data=f,
                file_name=os.path.basename(srt_path),
                mime="text/plain"
            )

        # Cleanup (safe after the user has had a chance to download)
        try:
            os.remove(audio_path)
            os.remove(video_path)
            os.remove(srt_path)
        except Exception:
            pass
