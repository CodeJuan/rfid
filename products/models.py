from django.db import models

# Create your models here.
class RFID(models.Model):
    RFID = models.CharField(max_length=12)
    AntennaID = models.CharField(max_length=20)

class Proxy(models.Model):
    ShopID = models.CharField(max_length=20)
    ProxyID = models.CharField(max_length=20)