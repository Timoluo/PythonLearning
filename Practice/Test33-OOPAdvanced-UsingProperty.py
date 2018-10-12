
### 使用@property

# 为了限制参数的合理性与范围，可以通过函数检查、设置；用另一个来获取
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

## Python内置的@property装饰器能把方法变成属性调用
# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter    #这个装饰器把 setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

## 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
## @property 和 setter对应，要先定义property才有后者


## 小结
## @property广泛应用在类的定义中，可以让调用者写出简短的代码，
#  同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

## 练习

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

# -*- coding: utf-8 -*-
class Screen(object):
     def __init__(self):   #由于实例调用时，未赋值，故直接定义初始值
        self.height = 0   
        self.width  = 0
 
    @property
    def resolution(self):
       return self.height*self.width
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

#繁杂写法
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property 
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height
