
````md
# Driver Distraction Detection using YOLO

## Project Description
This project detects driver distraction using a trained YOLO object detection model.  
The system focuses on identifying two classes only:
- **Using of Phone while Driving**

The model works in real-time using a webcam and helps in monitoring unsafe driving behavior.

---

## Features
- Real-time camera-based detection
- Focused on mobile phone usage while driving
- High precision and recall
- Lightweight and easy to run

---

## Requirements
Make sure the following are installed:

- Python 3.8 or above
- OpenCV
- Ultralytics (YOLO)
- Streamlit

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

