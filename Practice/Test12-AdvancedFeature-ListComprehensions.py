### 列表生成式

## Python内置的非常简单+强大的的用来创建list的生成式

>>> list(range(1, 11))     #range会取不到最后一位数
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

>>> L = []
>>> for x in range(1, 11):
...    L.append(x * x)
...
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表生成式则可以用一行语句代替循环生成上面的list：

>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

## 还可以使用两层循环，可以生成全排列：  #三层以上也可以，但可维护性很差
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C

## 因此，列表生成式也可以使用两个变量来生成list：

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']


#最后把一个list中所有的字符串变成小写：
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']

## 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁


##练习

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'


# 使用内建的isinstance函数可以判断一个变量是不是字符串：
>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [v.lower() for i,v in enumerate L1  if isinstance(v,str)]
print('L2 =',L2)        #enumerate能像.item()一样，读取index和value

# L2 = [s.lower() for s in L1 if (isinstance(s,str))]


# we want to find first 10 (or any n) pythogorian triplets. A triplet (x, y, z)
# is called pythogorian triplet if x*x + y*y == z*z.
>>> pyt = ((x, y, z) for z in integers() for y in xrange(1, z) for x in range(1, y) if x*x + y*y == z*z)
>>> take(10, pyt)
#[(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20),
# (15, 20, 25),(7, 24, 25), (10, 24, 26), (20, 21, 29)]
