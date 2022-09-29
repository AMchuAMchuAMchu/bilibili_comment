# Description ==> TODO
# BelongsProject ==> bilibili_comment
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-29 20:43:59
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start
import datetime
import time

import numpy as np

start = datetime.datetime.now().second



for i in range(200000):
    num = np.random.randint(low=4,high=10)*0.1
    print(num)

end = datetime.datetime.now().second

print('耗时:',end - start,'秒~~')





