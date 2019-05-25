# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com

import pandas as pd

# 获得城市列表
city_list = []
with open('../AllData/city_list.txt','r',encoding='utf8') as fr:
    for line in fr.readlines():
        city_list.append(line.strip())
        city_list.append(line.strip()[0:-1])
# print(city_list)

# 获得hudong_pedia.csv信息
allLines = []
with open('../AllData/1hudong_pedia.csv', 'r', encoding='utf-8') as fr:
    # pass
    read = fr.readline()
    # readlines = fr.readlines()
    # print(len(readlines))
    count = 0
    while(read):
        split = read.split('","')
        count += 1
        split[0] = split[0][1:]
        split[-1] = split[-1][:-2]
        if len(split) == 7:
            allLines.append(split)
        else:
            print('error in line', count, 'with', len(split), 'items', split)
        read = fr.readline()
# 转存为DataFrame
data = pd.DataFrame(allLines[1:], columns=allLines[0])

with open('../AllData/target/city_weather.csv', 'w', encoding='utf8') as fw:
    fw.write('city,relation,weather\n')
    vis = []
    weather = []
    for i in range(len(data)):
        title = str(data['title'][i]).strip()
        if (title in city_list):
            info_key = str(data['baseInfoKeyList'][i]).strip()
            if (len(info_key) == 0):
                continue
            info_value = str(data['baseInfoValueList'][i]).strip()
            info_key_list = info_key.split('##')
            info_value_list = info_value.split('##')
            cnt = 0
            for item in info_key_list:
                if (item.strip() == '气候条件：' or item.strip() == '气候：' or item.strip() == '气候条件' or item.strip() == '气候'
                        or item.strip() == '气候条件:' or item.strip() == '气候:'):
                    if (title[-1] != '市'):
                        title += '市'
                    if (title not in vis):
                        vis.append(title)
                        if (len(info_value_list[cnt].strip().split('、')) > 1):
                            for x in info_value_list[cnt].strip().split('、'):
                                if (x not in weather):
                                    weather.append(x)
                                fw.write(title + ",气候," + x + '\n')

                        else:
                            if (info_value_list[cnt].strip() not in weather):
                                weather.append(info_value_list[cnt].strip())
                            fw.write(title + ",气候," + info_value_list[cnt].strip() + '\n')
                cnt += 1

with open('../AllData/static_weather_list.csv', 'w', encoding='utf8') as fw:
    fw.write('title\n')
    for item in weather:
        fw.write(item + '\n')

