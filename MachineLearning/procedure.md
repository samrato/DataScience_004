
---

````markdown
# 🎤 Voice Machine Learning Demo

This project is a **Streamlit app** that demonstrates a simple **voice-enabled machine learning application**.  
Users can **speak a number**, and a **trained linear regression model** predicts an output.  
It also provides **text-to-speech feedback** and a **text fallback input**.

---

## 🚀 Features

1. **Voice Input:** Records audio from your microphone using `sounddevice`.  
2. **Speech Recognition:** Converts spoken audio to text with `SpeechRecognition` and Google Web API.  
3. **ML Prediction:** Uses a trained **linear regression model** to predict the output for the spoken or typed number.  
4. **Text-to-Speech:** Announces the prediction or errors using `pyttsx3`.  
5. **Text Fallback:** Users can manually type a number if voice recognition fails.  
6. **Linux Friendly:** Works without JACK or PulseAudio, suitable for XFCE/ALSA systems.  

---

## 🛠️ Installation

1. Navigate to your project folder:

```bash
cd ~/DataScience_With_Willington_Juma/MachineLearning
````

2. Activate your Python virtual environment:

```bash
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install streamlit sounddevice scipy speechrecognition pyttsx3 scikit-learn
```

4. Run the Streamlit app:

```bash
streamlit run voice_ml_demo.py
```

---

## 📂 Code Explanation

### 1. **ML Model Training**

```python
xs = np.array([-1, 0, 1, 2, 3, 4]).reshape(-1, 1)
ys = np.array([-2, 1, 4, 7, 10, 13])
model = LinearRegression()
model.fit(xs, ys)
```

* Creates a **small sample dataset**.
* Trains a **linear regression model** to learn the pattern in the data.
* Used to **predict outputs** based on user input.

---

### 2. **Text-to-Speech Engine**

```python
engine = pyttsx3.init()
def speak(msg):
    engine.say(msg)
    engine.runAndWait()
```

* `pyttsx3` is an **offline TTS engine**.
* Announces predictions or error messages.
* Works without internet.

---

### 3. **Voice Recording Function**

```python
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
```

* Records audio from the microphone using **sounddevice**.
* `duration=5` seconds by default, `fs=44100` sampling rate.
* `sd.wait()` ensures the recording is complete before processing.

---

### 4. **Convert to PCM WAV**

```python
recording_int16 = np.int16(recording * 32767)
wav.write(temp_wav.name, fs, recording_int16)
```

* Converts `float32` array from sounddevice into **int16 PCM** format.
* Required for `SpeechRecognition` to correctly read WAV files.
* Saves a **temporary WAV file** for recognition.

---

### 5. **Speech Recognition**

```python
recognizer = sr.Recognizer()
with sr.AudioFile(temp_wav.name) as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio)
```

* Reads the temporary WAV file.
* Uses **Google Web API** to convert audio → text.
* Returns the spoken number as a string.
* Handles **unknown speech** or **request errors** gracefully.

---

### 6. **Streamlit UI**

```python
st.title("🎤 Voice Machine Learning Demo")
if st.button("🎙️ Speak a Number"):
    text = listen_voice()
```

* Provides a **button** to start recording.
* Shows progress messages like **“Processing your voice…”**.
* Displays success or error messages after recognition.

---

### 7. **Prediction & Feedback**

```python
number = float(text)
prediction = model.predict(np.array([[number]]))[0]
st.info(f"📈 Predicted Output: **{prediction}**")
speak(f"The model predicts {prediction}")
```

* Converts recognized text to **float**.
* Uses the **linear regression model** to predict output.
* Displays the prediction in Streamlit and announces it via TTS.

---

### 8. **Text Fallback Input**

```python
number_input = st.text_input("Or type a number if voice fails:")
```

* Lets users **type a number manually**.
* Ensures the app is functional even if voice recognition fails.

---

## ⚠️ Notes

1. Works best with a **built-in or USB microphone**.
2. If voice recognition fails, type the number in the **fallback input**.
3. `pyttsx3` TTS works offline on Linux, Windows, and macOS.
4. Adjust `duration` in `listen_voice()` to record longer or shorter clips.

---

## 🏁 Usage

1. Click **🎙️ Speak a Number**.
2. Speak a number clearly (e.g., `3` or `4.5`).
3. Wait for the prediction and TTS feedback.
4. Or type a number if voice recognition fails.

---

## 🔧 Troubleshooting

* **Recording fails:** Ensure your microphone is accessible:

```bash
arecord -l
```

* **TTS issues:** Make sure `pyttsx3` dependencies are installed (`espeak` for Linux).
* **SpeechRecognition fails:** Check internet connection (Google Web API is online).

---

This app demonstrates **integrating voice input, ML prediction, and TTS** in a **Streamlit app** that is **Linux-friendly**.

```

---


