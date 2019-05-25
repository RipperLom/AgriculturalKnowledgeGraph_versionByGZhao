# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com

from scrapy import cmdline

name = 'hudong'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())