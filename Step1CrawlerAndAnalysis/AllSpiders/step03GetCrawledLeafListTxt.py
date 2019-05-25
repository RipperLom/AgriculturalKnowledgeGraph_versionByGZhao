# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com

import urllib.request
from urllib.parse import quote,unquote
import re
from Step1CrawlerAndAnalysis.AllModels.neo4jModel import Neo4j

if __name__ == '__main__':
    neo = Neo4j()
    neo.connectDB()
    s = {}
    with open('../AllData/leaf_list.txt', 'r',
              encoding='utf-8') as fr:
        with open('../AllData/crawled_leaf_list.txt', 'w',
                  encoding='utf-8') as fw:
            for line in fr.readlines():
                itemname = line.split(' ')[1].strip()
                if neo.matchHudongItembyTitle(itemname) != None:
                    continue
                if itemname in s:
                    continue
                s[itemname] = 1
                fw.write(itemname + '\n')