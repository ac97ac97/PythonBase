# import enum
# class WeekDays(enum.Enum):
#     #枚举常来列表  无构造方法
#     MONDAY=1
#     TUSEDAY=2
#     WENSDAY=3
#     THURSDAY=4
#     FRIDAY=10
# day = WeekDays.FRIDAY
# print(day)
# print(day.value)
# print(day.name)

# 限制枚举类
# import enum
#
# @enum.unique
# class WeekDays(enum.IntEnum):
#     # 枚举常来列表  无构造方法
#     MONDAY = 1
#     TUSEDAY = 2
#     WENSDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#
#
# day = WeekDays.FRIDAY
# print(day)
# print(day.value)
# print(day.name)


#使用枚举类
import enum

@enum.unique
class WeekDays(enum.IntEnum):
    # 枚举常来列表  无构造方法
    MONDAY = 1
    TUSEDAY = 2
    WENSDAY = 3
    THURSDAY = 4
    FRIDAY = 5


day = WeekDays.MONDAY

# if day.name == 'MONDAY':
#     print("工作")
# elif day.name=='FRIDAY':
#     print('学习')
if day ==WeekDays.MONDAY:
    print("工作")

elif day ==WeekDays.FRIDAY:
    print("学习")