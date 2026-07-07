
import cv2
import numpy as np
import pytesseract
from ultralytics import YOLO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

model = None

def get_model():
    global model
    if model is None:
        model = YOLO('yolov8n.pt')
    return model

@api_view(['POST'])
def detect_objects(request):
    image = request.FILES.get('image')

    if not image:
        return Response({'error': 'No image uploaded'}, status=400)

    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    results = get_model()(frame)

    detected = []

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            label = get_model().names[cls]
            detected.append(label)

    return Response({
        'detected_objects': detected
    })


@api_view(['POST'])
def read_text(request):
    image = request.FILES.get('image')

    if not image:
        return Response({'error': 'No image uploaded'}, status=400)

    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    text = pytesseract.image_to_string(frame)

    return Response({
        'text': text
    })


@api_view(['GET'])
def navigation(request):
    direction = request.GET.get('direction', 'forward')

    message = f'Move {direction} safely'

    return Response({
        'voice_instruction': message
    })

from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "message": "Smart Vision API Running",
        "endpoints": [
            "/api/detect/",
            "/api/read-text/",
            "/api/navigation/"
        ]
    })
    
    def home_page(request):
        return render(request, 'index.html')


def detect_page(request):
    return render(request, 'detect.html')


def ocr_page(request):
    return render(request, 'ocr.html')


def navigation_page(request):
    return render(request, 'navigation.html')
from django.shortcuts import render
from django.http import JsonResponse

def home_page(request):
    return render(request, 'index.html')


def detect_page(request):
    return render(request, 'detect.html')


def ocr_page(request):
    return render(request, 'ocr.html')


def navigation_page(request):
    return render(request, 'navigation.html')
