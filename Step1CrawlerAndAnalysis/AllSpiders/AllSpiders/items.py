# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TreeNodeItem(scrapy.Item):
    label = scrapy.Field()#当前节点名称
    father = scrapy.Field()#父节点名称

class LeafItem(scrapy.Item):
    treeNode = scrapy.Field()#当前节点名称
    child = scrapy.Field()#子节点名称

class HudongItem(scrapy.Item):
    # Item 对应互动百科中的一个词条
    title = scrapy.Field()  #标题
    url = scrapy.Field()  #对于互动百科页面的链接
    image = scrapy.Field()  #图片
    openTypeList = scrapy.Field()  #开放分类列表
    detail = scrapy.Field()  #详细信息
    baseInfoKeyList = scrapy.Field()  #基本信息key列表
    baseInfoValueList = scrapy.Field()  #基本信息value列表