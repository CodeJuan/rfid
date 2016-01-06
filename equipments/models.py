# -*- coding:utf-8 -*-
from django.db import models
from shops.models import Shop


class RfidReader(models.Model):
    ip = models.GenericIPAddressField(protocol='IPv4', max_length=100,
                                      verbose_name='IP')
    port = models.PositiveIntegerField(u'端口')
    shop = models.ForeignKey(Shop, verbose_name=u'店铺')

    def __unicode__(self):
        return u'%s-%s' % (self.shop, self.ip)

    class Meta:
        verbose_name = u'RFID 读写器'
        verbose_name_plural = verbose_name


class Ant(models.Model):
    seq = models.IntegerField(u'天线号')
    reader = models.ForeignKey(RfidReader, verbose_name=u'RFID 读写器')
    mode = models.IntegerField(u'天线用途', choices=(
        (0, u'停用'),
        (1, u'监控'),
        (2, u'读卡'),
        ))

    def __unicode__(self):
        return u'%s-%s' % (self.reader, self.seq)

    class Meta:
        verbose_name = u'RFID 天线'
        verbose_name_plural = verbose_name
