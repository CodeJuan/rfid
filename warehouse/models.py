# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Warehouse(models.Model):
    """仓库"""
    name = models.CharField(u'仓库名称', max_length=100)
    addr = models.CharField(u'地址', max_length=100)
    admin = models.ForeignKey(User)
    contact = models.CharField(u'联系人', max_length=100)
    phone = models.CharField(u'电话', max_length=100)
    status = models.IntegerField(u'状态', choices=(
        (0, u'启用'),
        (1, u'停用'),
        ))
