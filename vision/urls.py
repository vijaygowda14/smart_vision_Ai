from django.urls import path

from .views import (
    live_camera_page,
    detect_objects,
)

urlpatterns = [

    path(
        '',
        live_camera_page
    ),

    path(
        'detect/',
        detect_objects
    ),

]