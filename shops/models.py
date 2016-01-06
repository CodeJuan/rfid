# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(u'店铺名称', max_length=100)
    addr = models.CharField(u'地址', max_length=100)
    admin = models.ForeignKey(User, verbose_name=u'管理员')
    contact = models.CharField(u'联系人', max_length=100)
    phone = models.CharField(u'电话', max_length=100)
    status = models.IntegerField(u'状态', choices=(
        (0, u'启用'),
        (1, u'停用'),
        ))

    def __unicode__(self):
        return u'%s(%s)' % (self.name, self.addr)

    class Meta:
        verbose_name = u'店铺'
        verbose_name_plural = verbose_name
