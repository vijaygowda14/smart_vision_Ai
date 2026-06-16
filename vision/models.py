
from django.db import models

class DetectionLog(models.Model):
    detected_object = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detected_object
