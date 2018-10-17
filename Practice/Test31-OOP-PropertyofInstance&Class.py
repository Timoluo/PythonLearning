
### 实例属性和类属性


## Python可以在类创建的实例上通过 实例变量、或者self变量 绑定任意属性

#定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。

>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student

## 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
## 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性


## 练习

# 给Student类增加一个类属性，每创建一个实例，该属性自动增加

# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1 #用self.count+=1仅会在方法内部生效，无法累加

## self.count是实例内部的，每换一个实例的话就是相当于实例内部的一个count参数+1，
## 因此新建的话就一直是1，Student.count是全局的变量，这个变量一直保存在，
## 没有变成新的实例的变量或者释放掉，因此可以一直累加。

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


## 小结
            
## 实例属性属于各个实例所有，互不干扰；
## 类属性属于类所有，所有实例共享一个属性；
## 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
