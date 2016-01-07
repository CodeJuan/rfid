# -*- coding:utf-8 -*-
from django.db import models
from shops.models import Shop
from django.contrib.auth.models import User

# Create your models here.
class RFID(models.Model):
    RFID = models.CharField(max_length=12)
    AntennaID = models.CharField(max_length=20)

class Proxy(models.Model):
    ShopID = models.CharField(max_length=20)
    ProxyID = models.CharField(max_length=20)


class CheckIn(models.Model):
    RFID = models.CharField(max_length=12)
    AntennaID = models.CharField(max_length=20)
    #User = models.ForeignKey(User, verbose_name=u'负责人')
    User = models.CharField(max_length=20)
    Date = models.DateTimeField(auto_now=True)
    Shop = models.ForeignKey(Shop, verbose_name=u'店铺')
    Weight = models.FloatField()
    #Photo =