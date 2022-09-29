# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 19:43:01
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import requests
import json

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}#伪装成浏览器，绕过反爬
# url='https://api.bilibili.com/pgc/review/short/list?media_id=5852&ps=20&sort=0'
url='https://api.bilibili.com/pgc/review/short/list?media_id=28229676&ps=20&sort=0'

# 发送get请求
w = requests.get(url, headers=headers).text
json_comment=json.loads(w)
total=json_comment['data']['list']#url中list中存储的内容
num=json_comment['data']['total']#total中的内容，一共有多少个url
s=json_comment['data']#url中的所有内容
j = 0
count = 0
lovely = open(file='d:/lovely.txt',encoding='utf-8',mode='w')
while j < num:
    total = json_comment['data']['list']
    for i in range(len(total)):
        count += 1
        comment = total[i]['content']#获取url中的评论
        lovely.writelines('%s >> %s'%(count,comment))
        lovely.write('\n')
        print(count,'>>',comment)
    j += 1
    next=json_comment['data']['next']#获取next中的内容
    next1 = str(next)
    url1 = url + '&cursor=' + next1
    response = requests.get(url1, headers=headers).text
    json_comment = json.loads(response)

lovely.close()