# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json, time

class AllspidersPipeline(object):
    def process_item(self, item, spider):
        return item

# ================================================================
# step 01 get treenode_list.txt 文件
class TreeNodePipeline(object):

    def process_item(self, item, spider):
        # spider filter
        if spider.name == 'treenode':
            i = item['label']
            self.file.write(i + '\n')
            self.file.flush()
            pass
        return item


    def open_spider(self, spider):
        # spider filter
        if spider.name == 'treenode':
            self.file = open('../AllData/treenode_list.txt', 'w',
                             encoding ='utf-8')
            self.file.write('农业' + '\n')
            pass

    def close_spider(self, spider):
        # spider filter
        if spider.name == 'treenode':
            self.file.close()
            pass
# ================================================================

# ================================================================
# step 02 get leafList.txt 文件
class LeafListPipeline(object):

    def process_item(self, item, spider):
        # spider filter
        if spider.name == 'leafList':
            self.file.write(item['treeNode'] + " " + item['child']
                            + '\n')
            self.file.flush()
            pass
        return item

    def open_spider(self, spider):
        # spider filter
        if spider.name == 'leafList':
            self.file = open('../AllData/leaf_list.txt', 'w',
                            encoding='utf-8')
            pass

    def close_spider(self, spider):
        # spider filter
        if spider.name == 'leafList':
            self.file.close()
            pass
# ================================================================

# ================================================================
# get hudong.json 文件
class HudongPipeline(object):
    ##用于将hudongItem转化为json，并存到文件中

    def process_item(self, item, spider):
        # spider filter
        if spider.name == 'hudong':
            if item['title'] != 'error':  #'error'是百科中没有的页面
                # 赋予的title值（自己定义的）
                line = ""
                if (self.count > 0):
                    line += ","
                line += json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.file.write(line)
                self.count += 1
                cur = time.time()
                T = int(cur - self.start)
                print("page count: " + str(self.count) +
                      "      time:" + str(int(T / 3600)) + "h " + str(
                    int(T / 60) % 60) + "m " + str(T % 60) + "s......")
        return item
            # else:
            #     raise DropItem("百科中找不到对应页面！")

    def open_spider(self, spider):
        # spider filter
        if spider.name == 'hudong':
            self.count = 0
            self.file = open('../AllData/hudong_pedia.json',
                             'w', encoding='utf-8')
            self.start = time.time()
            self.file.write("[")
            print("==================开启爬虫 \"" + spider.name +
                  "\" ==================")

    def close_spider(self, spider):
        # spider filter
        if spider.name == 'hudong':
            self.file.write("]")
            self.file.close()
            print("==================关闭爬虫 \"" + spider.name +
                  "\" ==================")
# ================================================================

