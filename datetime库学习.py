import datetime
import time
d = datetime.date.today()
print(d,type(d))
d = datetime.date(2022, 8, 24)
print(d,type(d))
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)
print(d.year)
print(d.month)
print(d.day)
# datetime.date对象 -☞结构化时间对象
print(d.timetuple())

# 其他方法
# replace
print(d.replace(2022))
print(d.replace(d.year,9))
print(d.replace(day=20))
print(d.replace(d.year,d.month,20))
print(d.toordinal())
# 从0001-01-01到现在的天数
print(d.weekday())
print(d.isoweekday())
print(d.isoformat())
# 默认时间格式
# print(d.strftime("%y年%m月%d日"))

# print("========datetime.datetime=========")
# print("{:=<50s}".format("datetime.time"))

# time
t = datetime.time(15,10,45,888888)
print(t,type(t))
# 类方法
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

# shilishuxin
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
# 其他方法
print(t.isoformat())
# print(t.strftime("%Y时%M分%S秒 %f微秒"))

# datetime.datetime
# 生成时间日期
dt = datetime.datetime(2020,8,20,13,22,34,888888)
print()