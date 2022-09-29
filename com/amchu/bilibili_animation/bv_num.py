# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 19:45:19
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from bilibili_api import bangumi, sync

#
# 总之就是非常可爱：第2话 初夜#哔哩哔哩动画# https://www.bilibili.com/
# bangumi/play/ep341245/?share_medium=web&share_source=weibo&
# bbid=9DFC321E-25C8-477A-927C-42508EDBAFB8148797infoc&ts=1664451989325

async def main():
    b = await bangumi.get_episode_info(341245)
    # 打印 bv 号
    print(b)


sync(main())
