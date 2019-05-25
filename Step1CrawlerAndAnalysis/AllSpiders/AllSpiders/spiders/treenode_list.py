# -*- coding: utf-8 -*-
import scrapy

from Step1CrawlerAndAnalysis.AllSpiders.AllSpiders.items import TreeNodeItem
from urllib import parse
class TreeNodeSpider(scrapy.Spider):
    name = 'treenode'
    label = '农业'
    allowed_domains = ['fenlei.baike.com']

    def start_requests(self):
        yield scrapy.Request('http://fenlei.baike.com/' + self.label +
							 '/', meta={'father':self.label})

    def parse(self, response):
        item = TreeNodeItem()
        if response.xpath('//*[@class="sort"]/div/p[2]/a/text()').extract():
            sub = response.xpath('//*[@class="sort"]/div/p[2]/a/text()').extract()
        elif response.xpath('//*[@class="sort"]/h3[2]/text()').extract():
            sub = response.xpath('//*[@class="sort"]/p[2]/a/text()').extract()
        else:
            print(parse.unquote(response.url) + '无下级分类')
            return
        for i in sub:
            yield scrapy.Request(url='http://fenlei.baike.com/' + i + '/', meta={'father': i})
            item['label'] = i
            item['father'] = response.meta['father']
            yield item


