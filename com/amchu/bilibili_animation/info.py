# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 19:18:27
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from bilibili_api import Credential

credential = Credential(sessdata="a5ccf3b6%2C1673400132%2C9cfb1*71",
                        bili_jct="3ab7092e3181c71bf6b0f1ebd869f9a2",
                        buvid3="9DFC321E-25C8-477A-927C-42508EDBAFB8148797infoc")
print(credential.sessdata)
print(credential.bili_jct)
print(credential.buvid3)
