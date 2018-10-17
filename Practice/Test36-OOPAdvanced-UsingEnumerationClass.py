
### 使用枚举类


## 为月份这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
# Python提供了Enum类来实现这个功能：

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', ... , 'Nov', 'Dec'))

# 获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    
## value属性则是自动赋给成员的int常量，默认从1开始计数。
    
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
## @unique装饰器可以帮助我们检查保证没有重复值。


## 访问枚举类额若干方法
>>> print(Weekday.Tue)
Weekday.Tue
>>> print(Weekday['Tue'])
Weekday.Tue
>>> print(Weekday.Tue.value)
2
>>> print(Weekday(1))
Weekday.Mon
>>> day1 = Weekday.Mon
>>> print(day1 == Weekday(1))
True
## 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量


##练习

# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

# -*- coding: utf-8 -*-
from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender   # 直接跑也可以过，只是python会默默转化参数类型
        if type(gender) == Gender: # 用判断过滤非Gender类型，isinstance也可以
            self.gender = gender
        else:
            raise ValueError('gender type error')

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

## 小结
## Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
