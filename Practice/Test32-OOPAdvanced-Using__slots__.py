
### 面向对象高级编程

## 多重继承、定制类、元类等



### 使用__slots__

# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性.

# 给实例绑定一个方法：

>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25 

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 为了给所有实例都绑定方法，可以给class绑定方法;给class绑定方法后，所有实例均可调用：

>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score

## 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。



## Python允许在定义class的时候，定义个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 当尝试绑定__slots__定义以外的属性时，会得到AttributerError

## __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
## 除非在子类中也定义__slots__，
## 这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。


## implement

class Student(object):
    pass

def set_name(self, name):
    self.name = name

def set_age(self, age):
    self.age = age
    
#将方法绑定在类上
Student.set_name = MethodType(set_name,Student)
s1 = Student()
s2 = Student()
s3 = Student()
s1.set_name('tom')
s2.set_name('tony')
>>> print s1.name, ',', s2.name, ',', s3.name
tony , tony , tony

## MethodType给实例绑定方法时，方法不会影响到其他实例或者类；
## 但给类绑定方法时，在多个实例调用方法，最后一次调用会覆盖之前赋予的值

#给类增加属性二
Student.set_age = set_age
Student.set_age(Student, 55)
print(Student.age) #55
s4 = Student()
s5 = Student()
s4.set_age(66)
s5.set_age(77)
print(s4.age, s5.age) #66 #77 互不干扰


## 将方法绑定给类后，类和实例都可以调用和访问属性与方法，这不受slots范围限制
## 方法没有绑定给类而直接绑定给实例时，需要在slots规定范围中加入该方法和方法中的属性
