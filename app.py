import streamlit as st
from ultralytics import YOLO
import tempfile
from PIL import Image
import json
import os

# -------------------------------
# CONFIG
# -------------------------------
MODEL_PATH = "runs/detect/train/weights/best.pt"   # <-- update if needed

# Load YOLO11 model
model = YOLO(MODEL_PATH)

# -------------------------------
# STREAMLIT UI SETTINGS
# -------------------------------
st.set_page_config(page_title="YOLO11 Phone Detection", layout="wide")
st.title("YOLO11s  MODEL-1")
st.write("Upload an image to detect phone instances and generate detailed JSON output.")

# -------------------------------
# IMAGE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:

    # Show uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.getvalue())
        temp_input_path = tmp.name

    # -------------------------------
    # RUN YOLO PREDICTION
    # -------------------------------
    results = model.predict(temp_input_path, save=False, conf=0.25)
    result = results[0]

    # -------------------------------
    # DETAILED JSON GENERATION
    # -------------------------------
    detections = []

    for box in result.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]

        detection_info = {
            "class_id": cls_id,
            "class_name": cls_name,
            "confidence": float(box.conf[0]),
            "bbox_xyxy": {
                "x1": float(box.xyxy[0][0]),
                "y1": float(box.xyxy[0][1]),
                "x2": float(box.xyxy[0][2]),
                "y2": float(box.xyxy[0][3])
            },
            "bbox_xywh": {
                "x": float(box.xywh[0][0]),
                "y": float(box.xywh[0][1]),
                "width": float(box.xywh[0][2]),
                "height": float(box.xywh[0][3])
            }
        }
        detections.append(detection_info)

    output_json = {
        "model": "YOLO11s (Phone Detection)",
        "version": "Ultralytics 8.3.0+",
        "input_image": uploaded_file.name,
        "num_detections": len(detections),
        "detections": detections
    }

    # -------------------------------
    # SAVE & DISPLAY OUTPUT IMAGE
    # -------------------------------
    output_dir = tempfile.mkdtemp()
    output_image_path = os.path.join(output_dir, "output.jpg")
    result.save(filename=output_image_path)

    st.subheader("📌 Detection Result")
    st.image(output_image_path, caption="Detected Image", use_column_width=True)

    # -------------------------------
    # SHOW JSON IN APP
    # -------------------------------
    st.subheader("📝 Detailed Detection JSON")
    st.json(output_json)

    # -------------------------------
    # JSON DOWNLOAD BUTTON
    # -------------------------------
    st.download_button(
        label="Download JSON",
        data=json.dumps(output_json, indent=4),
        file_name="detection_output.json",
        mime="application/json"
    )
