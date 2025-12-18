
````md
🚗 Driver Distraction Detection using YOLO
📌 Project Overview

This project detects driver distraction in real time using a trained YOLO object detection model.
It is specifically optimized to identify mobile phone usage while driving, helping monitor unsafe driving behavior and improve road safety.

The system works with a live webcam feed and provides fast, accurate detection suitable for real-time applications.

🎯 Detection Classes

The model is trained to detect the following class:

Using Phone While Driving

Note: The model is intentionally focused on a single high-risk distraction to improve accuracy and reduce false positives.

✨ Features

Real-time driver monitoring using webcam

High precision detection for phone usage

Lightweight YOLO model for fast inference

Simple and clean Streamlit interface

Easy to set up and run locally

🛠️ Tech Stack

Python

YOLO (Ultralytics)

OpenCV

Streamlit

⚙️ Requirements

Ensure you have the following installed:

Python 3.8 or above

OpenCV

Ultralytics (YOLO)

Streamlit

Install dependencies:
```bash
pip install ultralytics opencv-python streamlit
````

---

## How to Train YOLO11n

```bash
yolo detect train model=yolo11n.pt data=data.yaml epochs=50 imgsz=640
```

---

## After Training the Best Model Will Be Saved At

```text
runs/detect/train/weights/best.pt
```

---

## Testing on Webcam

```bash
yolo detect predict model=runs/detect/<your_yolo11_folder>/weights/best.pt source=0 show=True
```

---

## Testing on App

```bash
streamlit run app.py
```

