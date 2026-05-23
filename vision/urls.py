from django.urls import path
from .views import (
    detect_objects,
    read_text,
    navigation,
    home_page,
    detect_page,
    ocr_page,
    navigation_page,
)

urlpatterns = [
    path('', home_page),
    path('detect-page/', detect_page),
    path('ocr-page/', ocr_page),
    path('navigation-page/', navigation_page),

    path('detect/', detect_objects),
    path('read-text/', read_text),
    path('navigation/', navigation),
]
