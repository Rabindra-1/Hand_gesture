# 🖐️ AI Hand Gesture Mouse Controller

A computer vision-based **touchless mouse control system** that allows users to control their computer cursor and perform mouse actions using only hand gestures through a webcam.

This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to detect hand movements, recognize gestures, and translate them into computer mouse operations.

The goal of this project is to create a natural, AI-powered, and contactless way of interacting with computers.

---

## ✨ Features

- 🖐️ Real-time hand tracking using webcam
- 🖱️ Move mouse cursor using index finger movement
- 👆 Left click using thumb-index finger pinch gesture
- 👆 Double click detection
- 📸 Screenshot capture using hand gestures
- 🎯 Smooth cursor movement
- ✋ Real-time hand landmark visualization
- 🚫 Cursor freeze during click detection
- ⚡ Fast real-time gesture processing

---

# 🛠️ Technologies Used

- **Python**
- **Computer Vision**
- **Artificial Intelligence**
- **Hand Gesture Recognition**
- **Automation**

---

# 📚 Libraries Used

| Library | Purpose |
|---------|---------|
| **OpenCV (`cv2`)** | Used for webcam access, image processing, frame conversion, flipping frames, and displaying the video stream |
| **MediaPipe** | Used for real-time hand detection and extracting 21 hand landmarks |
| **PyAutoGUI** | Used for controlling mouse movement, mouse clicks, and taking screenshots |
| **Math** | Used for calculating distance between hand landmarks for gesture recognition |
| **Time** | Used for click cooldown, double click detection, and timing operations |

---

# 📂 Project Structure

```
AI-Hand-Gesture-Mouse/
│
├── hand_mouse.py          # Main Python application
├── requirements.txt       # Required Python dependencies
└── README.md              # Project documentation
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Rabindra-1/hand_gesture.git
```

Navigate into the project folder:

```bash
cd hand_gesture
```

---

## 2. Create Virtual Environment (Recommended)

Create environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

Install required libraries:

```bash
pip install -r requirements.txt
```

# ▶️ Running the Project

Run the application:

```bash
python hand_gesture.py
```

After running:

1. Webcam will open
2. Hand landmarks will be detected
3. Move your hand to control the cursor
4. Use gestures for mouse actions

To exit the program:

Press:

```
q
```

---

# 🖐️ Gesture Controls

## 🖱️ Move Cursor

Gesture:

```
Move Index Finger
```

The system tracks the index fingertip position and maps it to the screen coordinates.

---

## 👆 Left Click

Gesture:

```
Thumb + Index Finger Pinch
```

When the distance between the thumb tip and index fingertip becomes small, the system performs a mouse click.

---

## 👆 Double Click

Gesture:

```
Perform Pinch Twice Quickly
```

The system detects two quick click gestures and performs a double click.

---

## 📸 Screenshot Capture

Gesture:

```
Close All Fingers
```

When all fingers are folded, the system automatically captures a screenshot.

Generated file:

```
screenshot.png
```

---

# 🧠 How It Works

The project follows this computer vision pipeline:

```
              Webcam
                 |
                 ↓
        Capture Video Frames
                 |
                 ↓
              OpenCV
                 |
                 ↓
        MediaPipe Hand Tracking
                 |
                 ↓
        Extract Hand Landmarks
                 |
                 ↓
        Gesture Recognition
                 |
                 ↓
          PyAutoGUI Actions
                 |
                 ↓
       Mouse Control / Screenshot
```

---

# ✋ Hand Landmark Detection

MediaPipe detects **21 different hand landmarks**.

This project uses the following landmarks:

| Landmark ID | Hand Point |
|-------------|------------|
| 4 | Thumb Tip |
| 8 | Index Finger Tip |
| 12 | Middle Finger Tip |
| 16 | Ring Finger Tip |
| 20 | Pinky Tip |

---

# 📐 Gesture Detection Logic

The system calculates the distance between thumb and index finger:

```
distance = √((x₂-x₁)² + (y₂-y₁)²)
```

If the distance is below the defined threshold:

```
distance < 0.06
```

The system recognizes it as a click gesture.

---

# 🎯 Cursor Movement Algorithm

The index fingertip coordinates from MediaPipe are converted into screen coordinates:

```
Camera Coordinates
        |
        ↓
Normalize Position
        |
        ↓
Convert to Screen Resolution
        |
        ↓
Move Mouse Cursor
```

A smoothing technique is applied to reduce cursor shaking and improve accuracy.

---

# 🚀 Future Improvements

- [ ] Add right-click gesture
- [ ] Add scrolling gesture
- [ ] Add drag and drop functionality
- [ ] Add volume control gestures
- [ ] Add brightness control gestures
- [ ] Improve cursor smoothing algorithm
- [ ] Add gesture customization
- [ ] Add multi-hand support
- [ ] Add GUI configuration panel
- [ ] Add gesture training system using Machine Learning

---

# ⚠️ Limitations

- Requires a working webcam
- Performance depends on lighting conditions
- Hand tracking accuracy depends on camera quality
- Cursor movement may require calibration
- Background noise can affect detection performance

---

# 📸 Demo

Add your project demo GIF/video here:

```
![Demo](demo.gif)
```

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Make your changes
4. Commit changes

```bash
git commit -m "Add new feature"
```

5. Push changes

```bash
git push origin feature-name
```

6. Create a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---
