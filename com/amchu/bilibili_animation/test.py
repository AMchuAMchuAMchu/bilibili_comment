# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 19:01:50
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


from bilibili_api import comment,sync


async def main():
    # 存储评论
    comments = []
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(418788911, comment.ResourceType.VIDEO, page)
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





