# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from django_thumbs.db.models import ImageWithThumbsField
from shops.models import Shop
from django.contrib.auth.models import User


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
    weight = models.FloatField(u'重量 (g)')
    photo = ImageWithThumbsField(upload_to=settings.PRODUCT_PHOTO,
                                 sizes=((200, 200), (450, 450)))
    shop = models.ForeignKey(Shop, verbose_name=u'门店')  # read by ant ID

    # basic info
    name = models.CharField(u'名称', max_length=100)
    status = models.ForeignKey(ProductStatus, verbose_name=u'状态')
    notes = models.CharField(u'备注', max_length=100, null=True, blank=True)
    scale = models.CharField(u'尺寸 (mm)', max_length=100, null=True, blank=True)

    # detail info
    style = models.ForeignKey(ProductStyle, verbose_name=u'样式')
    material = models.ForeignKey(ProductMaterial, verbose_name=u'材质')

    def __unicode__(self):
        return u'%s(%s)' % (self.name, self.weight)

    class Meta:
        verbose_name = u'物件单品'
        verbose_name_plural = verbose_name


# ------------------------ Actions ---------------------------

class OpType(models.Model):
    order = models.IntegerField(u'序号')
    name = models.CharField(u'名称', max_length=100)
    operate = models.IntegerField(u'操作环节',
                                  choices=(
                                      (1, u'入库'),
                                      (2, u'出库'),
                                      (3, u'上下柜'),
                                      (4, u'退货'),
                                      ))
    desc = models.CharField(u'备注', max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'操作类型'
        verbose_name_plural = verbose_name


class Operation(models.Model):
    tracking_no = models.IntegerField(u'操作单号')  # 自动加 1，所有操作使用一个计数器
    rfid = models.CharField(u'RFID 标签', max_length=100)
    product = models.ForeignKey(ProductItem, verbose_name=u'物件')
    operator = models.ForeignKey(User, verbose_name=u'操作员')
    op_type = models.ForeignKey(OpType, verbose_name=u'操作类型')
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s(%s)' % (self.op_type, self.tracking_no)

    class Meta:
        abstract = True


class ShopIn(Operation):
    shop = models.ForeignKey(Shop, verbose_name=u'入库门店')  # read by ant ID
    source = models.CharField(u'发货人', max_length=100,
                              null=True, blank=True)
    source_phone = models.CharField(u'发货人电话', max_length=100,
                                    null=True, blank=True)

    class Meta:
        verbose_name = u'入库单'
        verbose_name_plural = verbose_name


class ShopOut(Operation):
    shop = models.ForeignKey(Shop, verbose_name=u'出库门店')  # read by ant ID
    target = models.CharField(u'收货人', max_length=100,
                              null=True, blank=True)
    target_phone = models.CharField(u'收货人电话', max_length=100,
                                    null=True, blank=True)
    target_shop = models.CharField(u'收货仓库', max_length=100,
                                   null=True, blank=True)

    class Meta:
        verbose_name = u'出库单'
        verbose_name_plural = verbose_name


class ShelfOnOff(Operation):
    shop = models.ForeignKey(Shop, verbose_name=u'门店')  # read by ant ID

    class Meta:
        verbose_name = u'上柜/下柜记录'
        verbose_name_plural = verbose_name
