Here is a **clean, professional, and well-structured rewrite** of your README.
I have corrected grammar, improved flow, and made it consistent with the technical quality of your training/testing sections, **without changing your core content**.

You can **copy–paste this directly** 👇

---

````md
# 🚗 Driver Distraction Detection using YOLO

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

Install dependencies:
```bash
pip install ultralytics opencv-python streamlit
````

---

## 🏋️‍♂️ How to Train YOLO11n

Train the YOLO11n model using the following command:

```bash
yolo detect train model=yolo11n.pt data=data.yaml epochs=50 imgsz=640
```

---

## 💾 Model Output

After training, the best-performing model will be saved at:

```text
runs/detect/train/weights/best.pt
```

---

## 🎥 Testing on Webcam

Run inference directly using your webcam:

```bash
yolo detect predict model=runs/detect/<your_yolo11_folder>/weights/best.pt source=0 show=True
```

---

## 🖥️ Testing Using Streamlit App

Launch the Streamlit application:

```bash
streamlit run app.py
```

```

---

### ✅ Improvements Made
- Fixed grammatical issues (e.g. *“Using of Phone” → “Using Phone”*)
- Improved technical clarity and professionalism
- Better section naming and flow
- Hackathon / evaluator ready
- Industry-standard README structure

If you want, I can also:
- Add **performance metrics (mAP, precision, recall)**
- Make it **research-paper ready**
- Optimize it for **GitHub showcase & resume**

Just tell me 👍
```
