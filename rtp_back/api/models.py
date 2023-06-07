from django.db import models

# Create your models here.
class parking(models.Model):
    lugar=models.CharField(max_length=10)
    tiempo=models.CharField(max_length=10)