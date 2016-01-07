# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse


def site_info(request):
    return {'brand_logo': 'DjangoStart',  # show in navbar
            'nav_list': (
                ('/', u'RFID 监控'),
                ('#', u'RFID 列表'),
                ('#', u'入库'),
                ('#', u'盘点'),
                ('#', u'出库'),
                ('#', u'上柜 下柜'),
                (reverse('shops_home'), u'门店'),
                ('/admin', u'管理台'),
                ),
            }
