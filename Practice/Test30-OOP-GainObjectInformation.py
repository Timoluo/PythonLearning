
### 获取对象信息



## 使用type()

## 基本类型都可以用type()来判断
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>

## 如果一个变量指向函数或者类，也可以用type()判断：
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>

# 如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
>>> type('abc')==type(123)
False

#判断函数可以用types定义的常量
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True



## 使用isinstance（）

## isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上

#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True



## 使用dir()

## 使用dir()函数可获得一个对象的所有属性和方法，它返回一个包含字符串的list，
#  比如，获得一个str对象的所有属性和方法：
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
>>> len('ABC')
3
>>> 'ABC'.__len__()
3

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()

>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19

## 如果试图获取不存在的属性，会抛出AttributeError的错误：
#  可以传入一个default参数，如果属性不存在，就返回默认值：
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404

>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81


## 小结

## 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
## 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

#假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
#如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

## 在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
## 它可能是网络流，也可能是内存中的字节流，但只要read()方法返回有效的图像数据，就不影响功能。


## implement

bool(list) = True
bool(tuple) = True
#list 和 tuple 都有布尔值的
#所以
list or tuple = list
list and tuple = tuple
tuple or list = tuple
tuple and list = list


# 用到python的反射特性，判断是否存在多种方法

from command import MyObject

computer=MyObject()
def run(x):
    inp = input('method>')
    # 判断是否有这个属性
    if hasattr(computer,inp):
    # 有就获取然后赋值给新的变量
        func = getattr(computer,inp)
        print(func())
    else:
    # 没有我们来set一个
        setattr(computer,inp,lambda x:x+1)
        func = getattr(computer,inp)
        print(func(x))

if __name__ == '__main__':
    run(10)
#其实本章的内容，很多涉及到动态加载模块类
