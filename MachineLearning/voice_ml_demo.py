import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import speech_recognition as sr

# ---------------------------
# Train a simple ML model
# ---------------------------
xs = np.array([-1, 0, 1, 2, 3, 4]).reshape(-1, 1)
ys = np.array([-2, 1, 4, 7, 10, 13])
model = LinearRegression()
model.fit(xs, ys)

# ---------------------------
# Text-to-Speech Engine
# ---------------------------
engine = pyttsx3.init()
def speak(msg):
    engine.say(msg)
    engine.runAndWait()

# ---------------------------
# Voice Recognition Function
# ---------------------------
def listen_voice(duration=5, fs=44100):
    st.write(f"🎧 Recording for {duration} seconds...")
    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
    except Exception as e:
        st.error(f"❌ Could not record audio: {e}")
        return ""

    # Convert float32 (-1.0 to 1.0) → int16 PCM for SpeechRecognition
    recording_int16 = np.int16(recording * 32767)

    # Save to temporary WAV file
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav.write(temp_wav.name, fs, recording_int16)

    # Recognize speech
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_wav.name) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🎤 Voice Machine Learning Demo")
st.write("Speak a number and the ML model will predict the output!")

# Voice Input Button
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

# Optional Text Fallback
number_input = st.text_input("Or type a number if voice fails:")
if number_input:
    try:
        number = float(number_input)
        prediction = model.predict(np.array([[number]]))[0]
        st.info(f"📈 Predicted Output: **{prediction}**")
        speak(f"The model predicts {prediction}")
    except:
        st.error("❌ That is not a valid number.")
