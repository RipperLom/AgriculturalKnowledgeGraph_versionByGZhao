# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com

import json

# 打开文件
with open('../AllData/hudong_pedia.csv', 'w', encoding='utf-8') as fw:
    headers = ['"title"','"url"','"image"','"openTypeList"','"detail"','"baseInfoKeyList"','"baseInfoValueList"']
    headersList = ["title", "url", "image", "openTypeList", "detail", "baseInfoKeyList", "baseInfoValueList"]
    # csv第一行
    title = ','.join(headers)
    print(title)
    # 写入
    fw.write(title + '\n')
    with open('../AllData/1hudong_pedia.json', 'r', encoding='utf-8') as fp:
        # 获得所有信息
        hudongDicts = json.load(fp)
        print(len(hudongDicts))
        # 遍历每条信息
        for hudongDict in hudongDicts:
            # 每条csv
            lineInCsvList = []
            for header in headersList:
                detail = hudongDict[header]
                detail = detail.replace('\n', ' ').replace('\t', ' ')
                lineInCsvList.append('"' + detail + '"')
            lineInCsv = ','.join(lineInCsvList)
            fw.write(lineInCsv + '\n')





