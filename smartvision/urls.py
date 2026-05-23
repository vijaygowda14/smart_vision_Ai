
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Smart Vision Project Running Successfully")

urlpatterns = [
    path('', home),
    path('api/', include('vision.urls')),
]
