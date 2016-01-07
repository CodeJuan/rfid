# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse


def site_info(request):
    return {'brand_logo': 'DjangoStart',  # show in navbar
            'nav_list': (
                ('#', u'入库'),
                ('#', u'RFID 监控'),
                ('#', u'RFID 列表'),
                ('#', u'盘点'),
                ('#', u'出库'),
                ('#', u'上柜 下柜'),
                (reverse('shops_home'), u'门店管理'),
                ('#', u'部门和员工'),
                ('#', u'角色和权限'),
                ('#', u'设置'),
                ),
            }
