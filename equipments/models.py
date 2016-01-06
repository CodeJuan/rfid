# -*- coding:utf-8 -*-
from django.db import models
from warehouse.models import Warehouse


class RfidReader(models.Model):
    IP = models.GenericIPAddressField(protocol='IPv4', max_length=100, verbose_name='IP')
    port = models.PositiveIntegerField(u'端口')
    loc = models.ForeignKey(Warehouse, verbose_name=u'所属仓库')

    class Meta:
        verbose_name = u'RFID 读写器'
        verbose_name_plural = verbose_name


class Ant(models.Model):
    seq = models.IntegerField(u'天线号')
    reader = models.ForeignKey(RfidReader, verbose_name=u'RFID 读写器')
    status = models.IntegerField(u'状态', choices=(
        (0, u'启用'),
        (1, u'停用'),
        ))

    class Meta:
        verbose_name = u'RFID 天线'
        verbose_name_plural = verbose_name
