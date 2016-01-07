from django.db import models

# Create your models here.
class Report(models.Model):
    RFID = models.CharField(max_length=12)
    AntennaID = models.CharField(max_length=20)
    #IP from equipment