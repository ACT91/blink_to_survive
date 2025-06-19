# 🦖 Blink to Survive

**Blink to Survive** is a hands-free accessibility tool that lets you play the famous **Chrome Dino Game** using just your **eyes**!  
With a simple blink, your dinosaur will **jump over obstacles** — no keyboard or mouse needed.

---

## 🎯 Why This Project?

Whether you're having fun, exploring computer vision, or creating accessibility-friendly tech, *Blink to Survive* is designed to:

- ✅ Help users with limited mobility
- ✅ Explore real-time eye-blink detection
- ✅ Integrate AI into fun and practical gameplay

---

## 👁️ How It Works

1. **Webcam input** is captured using OpenCV
2. **MediaPipe FaceMesh** detects eye landmarks in real-time
3. A blink is detected using **EAR (Eye Aspect Ratio)**
4. If a blink is detected, the tool triggers a **Spacebar press**
5. Chrome Dino (`chrome://dino`) receives the input and jumps!

---

## 🧠 Tech Stack

| Tech          | Purpose                          |
|---------------|----------------------------------|
| Python 3.10+  | Main programming language        |
| OpenCV        | Webcam capture and display       |
| MediaPipe     | Real-time facial landmark detection |
| pynput        | Simulates keyboard input         |

---

## 🗂️ Project Structure

blink_to_survive/
├── main.py # Main application loop
├── camera_handler.py # Webcam handling (OpenCV)
├── blink_detector.py # MediaPipe + EAR-based blink logic
├── key_controller.py # Simulates spacebar press
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## 🚀 Installation

### 1. ✅ Install Python 3.10 or 3.11
Download from [python.org](https://www.python.org/downloads/)

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
If mediapipe doesn't install, ensure you're using Python 3.10–3.11 (not 3.13+).

🕹️ How to Use
Open Google Chrome and go to:
chrome://dino

Focus the game tab (click into the browser window)

Run the script:

bash
Copy
Edit
python main.py
When the webcam opens, look straight at it and blink once — the Dino jumps!

Press Esc or close the webcam window to quit.

📸 Screenshots
(Add your screenshots here once the tool is running)

📎 Known Issues
Blink detection may vary with lighting and webcam quality

Only one blink is counted per second (cooldown logic)

Doesn't work with Python 3.13+ due to lack of mediapipe support

❤️ Credits
MediaPipe by Google

OpenCV

pynput

🛠️ Future Features
Dual eye detection for better accuracy

Sound effects or feedback on blink

Game clone directly integrated in Python or Pygame

Package into .exe for portable offline play

📜 License
This project is open source under the MIT License.
Feel free to modify, enhance, and share!

✨ Demo Video (Coming Soon...)
