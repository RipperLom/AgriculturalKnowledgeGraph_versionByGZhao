# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com

import scrapy
from Step1CrawlerAndAnalysis.AllSpiders.AllSpiders.items import LeafItem
from urllib import parse
from urllib.parse import quote,unquote
from copy import deepcopy

class LeafListSpider(scrapy.Spider):
    name = 'leafList'
    allowed_domains = ['fenlei.baike.com']

    def start_requests(self):
        item = LeafItem()
        with open('../AllData/treenode_list.txt', 'r', encoding ='utf-8') as f:
            pre_str = 'http://fenlei.baike.com/'
            for u_str in f.readlines():
                u_str = u_str.strip()
                item['treeNode'] = u_str
                url = pre_str + u_str + r'/list'
                yield scrapy.Request(url, meta=deepcopy(item))

    def parse(self, response):
        item = response.meta
        children = response.xpath('//*[@id="all-sort"]/dl/dd/a/text()').extract()
        for child in children:
            item['child'] = child
            yield item

