import streamlit as st
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav
import pyttsx3
from sklearn.linear_model import LinearRegression
import speech_recognition as sr

# ---------------------------
# Train ML Model
# ---------------------------
xs = np.array([-1, 0, 1, 2, 3, 4]).reshape(-1, 1)
ys = np.array([-2, 1, 4, 7, 10, 13])
model = LinearRegression()
model.fit(xs, ys)

# ---------------------------
# Text-to-Speech
# ---------------------------
engine = pyttsx3.init()
def speak(msg):
    engine.say(msg)
    engine.runAndWait()

# ---------------------------
# Voice Recording with sounddevice
# ---------------------------
def listen_voice(duration=5, fs=44100):
    st.write(f"🎧 Recording for {duration} seconds...")
    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
    except Exception as e:
        st.error(f"❌ Could not record audio: {e}")
        return ""

    # Save to temp WAV
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav.write(temp_wav.name, fs, recording)

    # Recognize with SpeechRecognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_wav.name) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except:
        return ""

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🎤 Voice Machine Learning Demo")
st.write("Speak a number and the ML model will predict the output!")

if st.button("🎙️ Speak a Number"):
    st.write("Processing your voice...")

    text = listen_voice()

    if text.strip() == "":
        st.error("❌ I couldn't understand your speech. Please try again.")
        speak("I could not understand. Please try again.")
    else:
        st.success(f"🗣️ You said: {text}")
        try:
            number = float(text)
            prediction = model.predict(np.array([[number]]))[0]
            st.info(f"📈 Predicted Output: **{prediction}**")
            speak(f"The model predicts {prediction}")
        except:
            st.error("❌ That doesn't seem to be a valid number.")
            speak("That is not a valid number.")

# Optional: fallback text input
number_input = st.text_input("Or type a number if voice fails:")
if number_input:
    try:
        number = float(number_input)
        prediction = model.predict(np.array([[number]]))[0]
        st.info(f"📈 Predicted Output: **{prediction}**")
        speak(f"The model predicts {prediction}")
    except:
        st.error("❌ That is not a valid number.")
