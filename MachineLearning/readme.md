Install System Dependencies (PortAudio + Python Dev Headers)
sudo apt update
sudo apt install portaudio19-dev python3-devy


---

## **1️⃣ Make sure your virtual environment is activated**

You already have `(venv)` in your prompt, so that’s good.

---

## **2️⃣ Reinstall or bootstrap pip inside the venv**

Run:

```bash
python -m ensurepip --upgrade
```

This will install `pip` inside your virtual environment.

---

## **3️⃣ Upgrade pip**

```bash
python -m pip install --upgrade pip
```

---

## **4️⃣ Install Streamlit**

```bash
pip install streamlit
```

* After this, you can verify:

```bash
streamlit --version
```

* It should print the version installed.

---

## **5️⃣ Run Your App**

```bash
streamlit run voice_ml_demo.py
```

---

### ✅ Notes
