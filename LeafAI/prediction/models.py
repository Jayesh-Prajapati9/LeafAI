from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="predictions")
    plant_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=200)
    confidence = models.FloatField()
    image = models.ImageField(upload_to="predictions/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plant_name} - {self.disease}"
