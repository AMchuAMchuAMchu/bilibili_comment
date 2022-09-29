# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 19:01:50
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from bilibili_api import comment,sync


async def main():

    # < iframe
    # src = "//player.bilibili.com/player.html?aid=&bvid=BV1cv411M7fs&cid=437243409&page=1"
    # scrolling = "no"
    # border = "0"
    # frameborder = "no"
    # framespacing = "0"
    # allowfullscreen = "true" > < / iframe >

    # 总之就是非常可爱：第2话
    # 初夜  # 哔哩哔哩动画# https://www.bilibili.com/bangumi/play/ep341245/?share_medium=web&share_source=weibo&bbid=9DFC321E-25C8-477A-927C-42508EDBAFB8148797infoc&ts=1664451659356

    # 存储评论
    comments = []
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(251546717, comment.ResourceType.VIDEO, page)
        # 存储评论
        comments.extend(c['replies'])
        # 增加已获取数量
        count += c['page']['size']
        # 增加页码
        page += 1

        if count >= c['page']['count']:
            # 当前已获取数量已达到评论总数，跳出循环
            break

    # 打印评论
    for cmt in comments:
        print(f"{cmt['member']['uname']}: {cmt['content']['message']}")

    # 打印评论总数
    print(f"\n\n共有 {count} 条评论（不含子评论）")


sync(main())





