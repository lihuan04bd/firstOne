import time

import time, datetime

tss1 = '2013-10-10 23:40:00'
# 转为时间数组
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# current = time.strptime()
print(timeArray)

timeStamp = int(time.mktime(timeArray))
print(timeStamp)