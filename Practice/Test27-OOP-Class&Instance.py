
### 类和实例

## 类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，
# 每个对象都拥有相同的方法，但各自的数据可能不同

# (object)，表示该类是从哪个类继承下来的，
# 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类； Python一切皆对象

## 通过定义一个特殊的__init__方法，绑定属性
## 注意！ “__init__”前后分别由两个下划线！！！

## 方法的第一个参数永远是self，表示创建的实例本身；可以把各个属性都绑定到self上


## 数据封装

# 直接在类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
# 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
# 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节

# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


## 小结

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，
# 对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'

# bart.age=8,让bart有了age的属性
# 但是，lisa并没有age这个属性。

# bart和lisa两个实例变量，都是同一个类的实例，但是bart有的变量名包括姓名和成绩、年龄，
# lisa只有姓名和成绩。
