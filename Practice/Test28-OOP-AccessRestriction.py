
### 访问限制


## 要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#  在Python中，实例的变量名如果以__开头，
#  就变成了一个私有变量（private），只有内部可以访问，外部不能访问


## 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但当你看到这样的变量时，视为私有变量，不要随意访问”。

## 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：

>>> bart._Student__name
'Bart Simpson'
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

## 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。


## 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，
# 并检查参数有效性：

# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
        
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
