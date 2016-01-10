# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse


def site_info(request):
    return {'brand_logo': 'DjangoStart',  # show in navbar
            'nav_list': (
                ('/', u'RFID 监控'),
                ('/vivian/rfid-list', u'RFID 列表'),
                ('/vivian/warehouse-add', u'入库'),
                ('/vivian/product-check', u'盘点'),
                ('/vivian/warehouse-reduce', u'出库'),
                ('/vivian/on-off-shelves', u'上柜 下柜'),
                (reverse('shops_home'), u'门店'),
                ('/admin', u'管理台'),
                ),
            }
