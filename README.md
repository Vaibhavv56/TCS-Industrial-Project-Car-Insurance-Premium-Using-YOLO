# Driver Distraction Detection using YOLO

## 📌 Project Overview
This project implements a **real-time driver distraction detection system** using a trained **YOLO object detection model**.

The system is specifically designed to detect **mobile phone usage while driving**, which is one of the major causes of road accidents.  
By using a lightweight YOLO architecture, the model achieves **high accuracy and fast inference**, making it suitable for real-time webcam-based monitoring.

---

## 🎯 Detection Classes
The model is trained to detect the following class:

- **Using Phone While Driving**

> The focus on a single high-risk distraction helps improve precision and reduces false detections.

---

## ✨ Features
- Real-time webcam-based driver monitoring
- Accurate detection of mobile phone usage
- High precision and recall
- Lightweight and efficient YOLO model
- Simple and easy-to-run setup

---

## ⚙️ Requirements
Ensure the following are installed:

- Python 3.8 or above
- OpenCV
- Ultralytics (YOLO)
- Streamlit

Dataset link :
https://app.roboflow.com/vaibhavs-workspace-erdxx/phone_college_project-xoykn/1

Install dependencies:
```bash
pip install ultralytics opencv-python streamlit


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

