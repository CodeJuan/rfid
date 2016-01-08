# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from django_thumbs.db.models import ImageWithThumbsField
from shops.models import Shop


class ProductDetail(models.Model):
    order = models.IntegerField(u'序号')
    name = models.CharField(u'名称', max_length=100)
    desc = models.CharField(u'备注', max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class ProductStyle(ProductDetail):
    class Meta:
        verbose_name = u'款式'
        verbose_name_plural = verbose_name


class ProductMaterial(ProductDetail):
    class Meta:
        verbose_name = u'材质'
        verbose_name_plural = verbose_name


class ProductStatus(ProductDetail):
    class Meta:
        verbose_name = u'物件状态'
        verbose_name_plural = verbose_name


class ProductItem(models.Model):
    """SKU 单品表, 每个单品, 一个唯一的 RFID"""
    # read by hardware
    rfid = models.CharField(u'RFID 标签', max_length=100)
    weight = models.FloatField(u'重量(g)')
    photo = ImageWithThumbsField(upload_to=settings.PRODUCT_PHOTO,
                                 sizes=((150, 150), (450, 450)))
    shop = models.ForeignKey(Shop, verbose_name=u'门店')  # read by ant ID

    # basic info
    name = models.CharField(u'名称', max_length=100)
    status = models.ForeignKey(ProductStatus, verbose_name=u'状态')
    notes = models.CharField(u'备注', max_length=100, null=True, blank=True)
    scale = models.CharField(u'尺寸', max_length=100, null=True, blank=True)

    # detail info
    style = models.ForeignKey(ProductStyle, verbose_name=u'样式')
    material = models.ForeignKey(ProductMaterial, verbose_name=u'材质')

    def __unicode__(self):
        return u'%s(%s)' % (self.name, self.weight)

    class Meta:
        verbose_name = u'物件单品'
        verbose_name_plural = verbose_name


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
    # User = models.ForeignKey(User, verbose_name=u'负责人')
    User = models.CharField(max_length=20)
    Date = models.DateTimeField(auto_now=True)
    Shop = models.ForeignKey(Shop, verbose_name=u'店铺')
    Weight = models.FloatField()
    # Photo =
