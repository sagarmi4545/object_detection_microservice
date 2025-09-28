# AI Backend (FastAPI)
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import os

from ultralytics import YOLO
from PIL import Image
import shutil
import uuid

app = FastAPI()

# Load YOLOv8n model (Ultralytics, runs on CPU, downloads automatically)
model = YOLO('yolov8n.pt')

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/detect/")
async def detect(file: UploadFile = File(...)):
    # Save uploaded file
    temp_filename = f"temp_{uuid.uuid4().hex}_{file.filename}"
    temp_path = os.path.join(OUTPUT_DIR, temp_filename)
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run detection
    results = model(temp_path)
    boxes = results[0].boxes
    detections = []
    for box in boxes:
        xyxy = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        name = results[0].names[cls]
        detections.append({
            "class": name,
            "confidence": conf,
            "box": xyxy
        })

    # Save output image with bounding boxes
    output_img_path = os.path.join(OUTPUT_DIR, f"det_{file.filename}")
    result_img = results[0].plot()
    Image.fromarray(result_img).save(output_img_path)

    # Save JSON results
    json_path = os.path.join(OUTPUT_DIR, f"det_{os.path.splitext(file.filename)[0]}.json")
    with open(json_path, "w") as jf:
        import json
        json.dump(detections, jf, indent=2)

    # Clean up temp file
    os.remove(temp_path)

    return JSONResponse({
        "detections": detections,
        "output_image": os.path.basename(output_img_path),
        "output_json": os.path.basename(json_path)
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
