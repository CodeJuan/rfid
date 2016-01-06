# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Warehouse(models.Model):
    name = models.CharField(u'仓库名称', max_length=100)
    addr = models.CharField(u'地址', max_length=100)
    admin = models.ForeignKey(User, verbose_name=u'管理员')
    contact = models.CharField(u'联系人', max_length=100)
    phone = models.CharField(u'电话', max_length=100)
    status = models.IntegerField(u'状态', choices=(
        (0, u'启用'),
        (1, u'停用'),
        ))

    class Meta:
        verbose_name = u'仓库管理'
        verbose_name_plural = verbose_name
