import urllib.request
from bs4 import BeautifulSoup
import re

findcomment = re.compile(r'<span class="short">(.*)</span>')  # 根据网页的源代码写一个正则表达式,对应评论的文本

def GetTxt(start):
    url = 'https://movie.douban.com/subject/25804168/comments?percent_type=&start=' + \
             str(start) + '&limit=20&sort=new_score&status=P'
    head = {  # 模拟浏览器头部信息，向服务器发送消息。Firefox浏览器头部信息如下：
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    request = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(request)
    html_data = response.read().decode('utf-8')
    commentlist = []
    soup = BeautifulSoup(html_data, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        eachcomment = re.findall(findcomment, str(item))  # 如果不把item转换为str类型findall函数会报错
        print(eachcomment)  # 检查一下每一条爬取的是否正确
        commentlist.append(eachcomment)
    f = open('content.txt', 'a', encoding='utf-8')
    for comment in commentlist:
        if comment != []:  # 爬取过程发现有些是空列表
            f.write(comment[0])
            f.write('\n')
    f.close()


def main():
    for i in range(1, 201, 20):  # 原本想多爬取一些，但是网站只允许看到前200条，之后需要登录
        print(i)
        GetTxt(i)


if __name__ == '__main__':
    main()
