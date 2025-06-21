import streamlit as st
from summarizer import get_summarizer, summarize_text
from utils import read_pdf, read_txt
from audio_to_text import transcribe_with_whisper
from text_to_speech import generate_speech
from db import create_table, insert_summary, get_user_summaries


st.set_page_config(page_title="AI Text Summarizer", layout="wide")
st.title("🧠 AI Text Summarization App")


model_name = st.selectbox("Choose Model", ["t5", "bart"])
summarizer = get_summarizer(model_name)


input_type = st.radio("Select Input Type", ["Manual Text", "Upload File", "Speech Input"])

input_text = ""

if input_type == "Manual Text":
    input_text = st.text_area("Enter text to summarize:", height=300)

elif input_type == "Upload File":
    file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])
    if file:
        input_text = read_pdf(file) if file.name.endswith(".pdf") else read_txt(file)
        st.text_area("File Content", input_text, height=300)

elif input_type == "Speech Input":
    audio_file = st.file_uploader("Upload WAV file", type=["wav"])
    if audio_file:
        st.info("Transcribing audio...")
        input_text = transcribe_with_whisper(audio_file.read())
        st.text_area("Transcribed Text", input_text, height=300)


if st.button("Summarize"):
    if input_text:
        st.info("Generating summary...")
        summary = summarize_text(input_text, summarizer)
        st.subheader("📌 Summary")
        st.write(summary)

        
        st.subheader("🔊 AI Voice Output")
        audio_path = generate_speech(summary)
        st.audio(audio_path, format="audio/mp3")
    else:
        st.warning("Please provide input.")

