# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-11-06 10:06:09
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import requests
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}  # 伪装成浏览器，绕过反爬


res01 = requests.request(method='get',url='https://movie.douban.com/subject/25804168/comments?percent_type=&start=20&limit=20&status=P&sort=new_score&comments_only=1',headers=headers)

print(res01.ok)

res01.encoding = 'utf-8'

context01 = json.loads(res01.text)

content02 = context01['html']

res02 = BeautifulSoup(content02,'html.parser')


# print(content02)
i = 0
for item in res02.select('.short'):
    i += 1
    print(i,'>>',item.text)