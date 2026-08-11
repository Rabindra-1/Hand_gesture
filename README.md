# 🖐️ AI Hand Gesture Mouse Controller

A computer vision application that allows users to control their computer cursor and perform click actions using real-time hand gestures through a webcam.

Built with **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

---

## ✨ Features

- 🖱️ **Cursor Tracking:** Move mouse cursor using index finger positioning.
- 👆 **Left Click:** Trigger click via thumb and index finger pinch gesture.
- 👆 **Double Click:** Automatic detection of consecutive quick pinches.
- 📸 **Screenshot:** Fold all fingers inward to capture a full-screen screenshot (`screenshot.png`).

---

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV** — Frame capture and video processing
- **MediaPipe** — 21-point hand landmark extraction
- **PyAutoGUI** — Native OS cursor control and click automation

---

## 🚀 Quick Start

### 1. Clone & Set Up Environment

```bash
git clone [https://github.com/Rabindra-1/hand_gesture.git](https://github.com/Rabindra-1/hand_gesture.git)
cd hand_gesture

python -m venv venv
# On Windows: venv\Scripts\activate
# On Linux/macOS: source venv/bin/activate. '''


### 2. Install Dependencies
``` Bash
pip install -r requirements.txt
### 3. Run Application
``` bash
python hand_mouse.py
Press q in the video window to quit.
