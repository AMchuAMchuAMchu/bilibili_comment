# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 19:43:01
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
import datetime
import random

import requests
import json
import numpy as np


start = datetime.datetime.now().second

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}  # 伪装成浏览器，绕过反爬
# url='https://api.bilibili.com/pgc/review/short/list?media_id=5852&ps=20&sort=0'
url = 'https://api.bilibili.com/pgc/review/short/list?media_id=28229676&ps=20&sort=0'

# 发送get请求
w = requests.get(url, headers=headers).text
json_comment = json.loads(w)
total = json_comment['data']['list']  # url中list中存储的内容
num = json_comment['data']['total']  # total中的内容，一共有多少个url
print(num)
s = json_comment['data']  # url中的所有内容
j = 0
count = 0
lovely = open(file='d:/lovelyInfo.txt', encoding='utf-8', mode='w')
# head = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
#
# <body>'''
# lovely.write(head)
while count < num:
    total = json_comment['data']['list']
    for i in range(len(total)):
        # num01 = np.random.randint(low=0, high=256)
        # num02 = np.random.randint(low=0, high=256)
        # num03 = np.random.randint(low=0, high=256)
        # num04 = np.random.randint(low=4, high=10) * 0.1
        count += 1
        comment = total[i]['content']  # 获取url中的评论
        # lovely.writelines('<h1 style="background-color: rgba(%d,%d,%d,%f);color: rgba(%d,%d,%d,%f)">%s >> %s</h1>' % (
        # num01, num02, num03, num04, num01, num02, num03, num04, count, comment))
        lovely.writelines(comment)
        lovely.write('\n')
        print(count)
        # print(count, '>>', comment)
    next = json_comment['data']['next']  # 获取next中的内容
    next1 = str(next)
    url1 = url + '&cursor=' + next1
    response = requests.get(url1, headers=headers).text
    json_comment = json.loads(response)

# end = '''</body>
# </html>'''
# lovely.write(end)
end = datetime.datetime.now().second
print('耗时:',end - start,'秒')
lovely.close()
