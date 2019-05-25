# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com
from py2neo import Graph, Node, Relationship
from Step1CrawlerAndAnalysis.AllModels.hudong_class import HudongItem

class Neo4j():


    def __init__(self):
        self.graph = None
        pass
        # print("create neo4j class ...")

    def connectDB(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password="123456")
        print('Neo4j connect successed')

    def matchItembyTitle(self, value):
        answer = self.graph.find_one(label="Item", property_key="title", property_value=value)
        return answer

    # 根据title值返回互动百科item
    def matchHudongItembyTitle(self, value):
        answer = self.graph.find_one(label="HudongItem", property_key="title", property_value=value)
        return answer

    # 返回限定个数的互动百科item
    def getAllHudongItem(self, limitnum):
        List = []
        ge = self.graph.find(label="HudongItem", limit=limitnum)
        for g in ge:
            List.append(HudongItem(g))

        print('load AllHudongItem over ...')
        return List