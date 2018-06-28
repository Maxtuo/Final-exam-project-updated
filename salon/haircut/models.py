from django.db import models

# Create your models here.
class Appointment(models.Model):
     barber = models.CharField(max_length=180, null=True, blank=True)
     user = models.CharField(max_length=180, null=True, blank=True)
     time = models.CharField(max_length=180, null=True, blank=True)