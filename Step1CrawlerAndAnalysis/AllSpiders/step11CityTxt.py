# -*- coding: utf-8 -*-
# Design by zhaoguanzhi
# Email: zhaoguanzhi1992@163.com

import requests
from lxml import etree
url = 'http://www.yunlietou.com/citylist.html'
html = requests.get(url).content.decode('gb2312')
html = etree.HTML(html)
citys = html.xpath('/html/body/text()')
HugeCitys = html.xpath('/html/body/b/text()')

with open('../AllData/city_list.txt', 'w', encoding='utf-8') as f:
    for city in HugeCitys:
        city = city.replace(':', '')
        try:
            # 目标
            city.index('市')
        except:
            pass
        else:
            if not city == '直辖市':
                f.write(city + '\n')

    for city in citys:
        # 去除换行制表符
        city_replace = city.replace('\r', '').replace('\n', '').replace('\t', '')
        if not city_replace == '':
            try:
                # 目标行
                city_replace.index('市:')
            except:
                # 无用行
                pass
            else:
                # 去除空格和点
                clearInfo = city_replace.replace(' ', '').replace('.', '')
                # 去除标题
                cityInLine = clearInfo.split(':')[1]
                # 切分
                citysInLine = cityInLine.split(',')
                for target in citysInLine:
                    # 检查是否为空
                    if not target == '':
                        try:
                            # 信息完全
                            target.index('市')
                        except:
                            # 信息不完全
                            target += '市'
                        else:
                            target
                        finally:
                            f.write(target + '\n')




