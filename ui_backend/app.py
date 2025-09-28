
# UI Backend (FastAPI)
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
import shutil
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # Send to AI backend
    with open(temp_path, "rb") as img:
        response = requests.post("http://localhost:8001/detect/", files={"file": (file.filename, img, file.content_type)})
    os.remove(temp_path)
    result = response.json()
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

# To run: uvicorn app:app --host 0.0.0.0 --port 8000
