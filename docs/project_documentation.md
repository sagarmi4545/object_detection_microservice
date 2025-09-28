# Project Documentation: Object Detection Microservice

## Overview
This project implements a microservice architecture for object detection using a lightweight open-source model (YOLOv3). It consists of two main components:
- **UI Backend (Flask):** Accepts image uploads from users and communicates with the AI backend.
- **AI Backend (FastAPI):** Performs object detection using YOLOv3 and returns results in JSON format.

## Steps to Solution
1. **Project Structure:**
   - Created separate folders for `ai_backend`, `ui_backend`, `docker`, `docs`, and `output`.
2. **AI Backend:**
   - Used FastAPI for a simple REST API.
   - Will use Ultralytics YOLOv3 (CPU mode) for detection ([reference](https://github.com/ultralytics/yolov3)).
3. **UI Backend:**
   - Used Flask to provide a web interface for image upload.
   - Sends uploaded images to the AI backend and displays results.
4. **Containerization:**
   - Wrote Dockerfiles for both services.
   - Used `docker-compose` for orchestration.
5. **Output Handling:**
   - Detected images with bounding boxes and JSON results are saved in the `output/` folder.
6. **Documentation:**
   - This file and the `README.md` provide setup, usage, and reference information.

## References
- [ultralytics/yolov3](https://github.com/ultralytics/yolov3)
- FastAPI, Flask, Docker official docs

## Next Steps
- Implement detection logic in `ai_backend/main.py`.
- Implement file upload and result display in `ui_backend/app.py`.
- Test end-to-end flow and save outputs.

---
This documentation will be updated as the implementation progresses.
