# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 21:11:29
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import requests
from bs4 import BeautifulSoup
import time
import random

import jieba
import wordcloud
# 读取文本
with open("d:/lovelyInfo.txt",encoding="utf-8",mode='r') as f:
    s = f.read()
print(s)
ls = jieba.lcut(s) # 生成分词列表
text = ' '.join(ls) # 连接成字符串


stopwords = ["的","是","了"] # 去掉不需要显示的词

wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1920,
                         height = 1080,
                         background_color='white',
                         max_words=500,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("d:/lovely02.png") # 保存词云文件

