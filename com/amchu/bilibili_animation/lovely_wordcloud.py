# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 21:11:29
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import jieba
import wordcloud
# 读取文本
# with open("d:/lovelyInfo.txt",encoding="utf-8",mode='r') as f:
s = open(r"D:\_01_后端开发笔记\_04_Python以及遇到的各种问题\_02_bilibili_comment\_00_demo\_02_sao_season2\sao_season2.txt",encoding="utf-8",mode='r').read()

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
wc.to_file(r"D:\_01_后端开发笔记\_04_Python以及遇到的各种问题\_02_bilibili_comment\_00_demo\_01_sao_season1\sao_season01.png") # 保存词云文件

