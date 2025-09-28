# Object Detection Microservice

## Overview
This project consists of two microservices: a UI backend (Flask) and an AI backend (FastAPI) for object detection using YOLOv3. Both are containerized with Docker.

## Prerequisites
- Docker
- Python 3.9+

## Setup & Run
1. Clone the repo and navigate to the project folder.
2. Build and run with Docker Compose:
   ```
docker-compose up --build
   ```
3. Access the UI at http://localhost:8000

## Output
- Detected images and JSON results are saved in the `output/` folder.

## References
- [ultralytics/yolov3](https://github.com/ultralytics/yolov3)

## Documentation
See `docs/` for detailed steps and implementation notes.
