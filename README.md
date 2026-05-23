
# Smart Vision for Blind People (Django Project)

Features:
- Object Detection using YOLOv8
- OCR Text Reading
- Voice Guidance API
- Django REST API Backend

## Installation

```bash
pip install -r requirements.txt
```

## Run Django Server

```bash
python manage.py migrate
python manage.py runserver
```

## Object Detection API

POST `/api/detect/`

Send image file using form-data:
- key: image

## OCR API

POST `/api/read-text/`

## Voice Navigation API

GET `/api/navigation/?direction=left`
