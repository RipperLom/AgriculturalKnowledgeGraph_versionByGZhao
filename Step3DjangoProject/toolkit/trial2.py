# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com
def get_explain(s):
    if s == 1:
        return '人物'
    if s == 2:
        return '地点'
    if s == 3:
        return r'机构'
    if s == 4:
        return '政治经济名词'
    if s == 5:
        return '动物学名词'
    if s == 6:
        return '植物学名词'
    if s == 7:
        return '化学名词'
    if s == 8:
        return '季节气候'
    if s == 9:
        return '动植物产品'
    if s == 10:
        return '动植物疾病'
    if s == 11:
        return '自然灾害'
    if s == 12:
        return '营养成分'
    if s == 13:
        return '生物学名词'
    if s == 14:
        return '农机具'
    if s == 15:
        return '农业技术术语'
    if s == 16:
        return '其它实体'

    if s == 'np':
        return '人物'
    if s == 'ns':
        return '地点'
    if s == 'ni':
        return '机构'
    if s == 'nz':
        return '专业名词'
    if s == 'i' or s == 'id':
        return '习语'
    if s == 'j':
        return '简称'
    if s == 'x':
        return '其它'
    if s == 't':
        return '时间日期'

    return '非实体'
def get_detail_explain(s):
    if s == 1:
        return '包括人名，职位'
    if s == 2:
        return '包括地名，区域，行政区等'
    if s == 3:
        return '包括机构名，会议名，期刊名等'
    if s == 4:
        return '包括政府政策，政治术语，经济学术语'
    if s == 5:
        return '包括动物名称，动物类别，动物学相关术语'
    if s == 6:
        return '包括植物名称，植物类别，植物学相关术语'
    if s == 7:
        return '包括化肥，农药，杀菌剂，其它化学品，以及一些化学术语'
    if s == 8:
        return '包括天气气候，季节，节气'
    if s == 9:
        return '包括肉制品，蔬菜制品，水果制品，豆制品等以动植物为原料的食品，以及一些非食物制品'
    if s == 10:
        return '包括传染病，原发性疾病，遗传病等'
    if s == 11:
        return '包括一些大型灾害，环境污染，或其它造成经济损失的自然现象'
    if s == 12:
        return '包括脂肪，矿物质，维生素，碳水化合物，无机盐等'
    if s == 13:
        return '包括人体部位，组织器官，基因相关，微生物，以及一些生物学术语'
    if s == 14:
        return '包括用于农业生产的自动化机械，手工工具'
    if s == 15:
        return '包括农学名词，农业技术措施'
    if s == 16:
        return '与农业领域没有特别直接的关系，但是也是实体'

    if s == 'np':
        return '包括人名，职位'
    if s == 'ns':
        return '包括地名，区域，行政区等'
    if s == 'ni':
        return '包括机构名，会议名，期刊名等'
    if s == 'nz':
        return ' '
    if s == 'i' or s == 'id':
        return ' '
    if s == 'j':
        return ' '
    if s == 'x':
        return ' '
    if s == 't':
        return ' '

    return '非实体'
def preok(s):  # 上一个词的词性筛选

    if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
        return True
    if s == 'v' or s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 'u':
        return True
    if s == 't' or s == 'm':
        return True
    return False
def nowok(s):  # 当前词的词性筛选

    if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
        return True
    if s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 't':
        return True
    if s == 't' or s == 'm':
        return True
    return False
def temporaryok(s):  # 一些暂时确定是名词短语的（数据库中可以没有）
    if s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
        return True
    if s == 'j' or s == 'x' or s == 't':
        return True
    return False

import thulac
import os
import csv
# 拼接查找
matchSize = 4
thu1 = thulac.thulac()  #默认模式
text = '我觉的腹部不舒服，我想去风湿科，不知道是不是得的弗郎西丝菌肺炎'
TagList = thu1.cut(text, text=False)
for i in range(matchSize):
    TagList.append(['===',None])  #末尾加个不合法的，后面好写
print(TagList)

predict_labels = {}   # 预加载实体到标注的映射字典
filePath = os.getcwd()
with open('predict_labels.txt','r',encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		predict_labels[str(row[0])] = int(row[1])

with open('totalEntities.txt','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        try:
            predict_labels[str(row[0])] = int(row[1])
        except:
            print('非法数据：', row)

label = predict_labels
# print(label)

from Step3DjangoProject.Model.neo_models import Neo4j
db = Neo4j()  # 预加载neo4j
db.connectDB()

answerList = []
length = len(TagList) - matchSize # 扣掉多加的那个
print(length)
i = 0
while i < length:
    p1 = TagList[i][0]
    t1 = TagList[i][1]
    print(p1, t1)
    p2 = TagList[i+1][0]
    t2 = TagList[i+1][1]
    p3 = TagList[i+2][0]
    t3 = TagList[i+2][1]
    p4 = TagList[i+3][0]
    t4 = TagList[i+3][1]
    p5 = TagList[i+4][0]
    t5 = TagList[i+4][1]
    p12 = p1 + TagList[i+1][0]
    p123 = p12 + TagList[i+2][0]
    p1234 = p123 + TagList[i+3][0]
    p12345 = p1234 + TagList[i+4][0]

    # 不但需要txt中有实体，还需要判断数据库中有没有
    flag = db.matchHudongItembyTitle(p12345)
    # if p12345 in label and flag != None:  # 组合2个词如果得到实体
    if p12345 in label:  # 组合2个词如果得到实体
        answerList.append([p12345, label[p12345]])
        i += 5
        continue

    # 不但需要txt中有实体，还需要判断数据库中有没有
    flag = db.matchHudongItembyTitle(p1234)
    # if p1234 in label and flag != None:  # 组合2个词如果得到实体
    if p1234 in label:  # 组合2个词如果得到实体
        answerList.append([p1234, label[p1234]])
        i += 4
        continue

    # 不但需要txt中有实体，还需要判断数据库中有没有
    flag = db.matchHudongItembyTitle(p123)
    # if p123 in label and flag != None:  # 组合2个词如果得到实体
    if p123 in label:  # 组合2个词如果得到实体
        answerList.append([p123, label[p123]])
        i += 3
        continue

    # 不但需要txt中有实体，还需要判断数据库中有没有
    flag = db.matchHudongItembyTitle(p12)
    # if p12 in label and flag != None:  # 组合2个词如果得到实体
    if p12 in label:  # 组合2个词如果得到实体
        answerList.append([p12, label[p12]])
        i += 2
        continue

    flag = db.matchHudongItembyTitle(p1)
    # if p1 in label and flag != None and nowok(t1):  # 当前词如果是实体
    if p1 in label:  # 当前词如果是实体
        answerList.append([p1, label[p1]])
        i += 1
        continue

    if temporaryok(t1):
        answerList.append([p1, t1])
        i += 1
        continue

    answerList.append([p1, 0])
    i += 1
print(answerList)
