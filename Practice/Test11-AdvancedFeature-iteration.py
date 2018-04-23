### 迭代

## for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）

# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:            # key-value
...     print(key)  

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

## 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
## 如果要同时迭代key和value，可以用for k, v in d.items()


# 通过collections模块的Iterable类型判断是否为可迭代对象：

>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False

## enumerate函数可以把list变成索引-元素对，就可以实现for循环下标循环，同时迭代索引和元素本身
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)

# 没enumerate函数,会尝试返回tuple内的值
>>> for i, value in ([('A','B'),('D','C')]):
...     print(i, value)


>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)


## 练习

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

# -*- coding: utf-8 -*-
def findMinAndMax(L):

  if L==[]:
       print (None, None)
  elif len(L) == 1:       #可用赋予初始值替代省略
       print (L[0],L[0])
  else:   ## 用else替代 elif len(L) > 1: //list要用len()获取长度，而字符串直接就有.len
       (Min,Max) = (L[0],L[0])    
       for i,value in enumerate (L):
         if L[i] > Max:
            Max = value
         elif L[i] < Min:   ## 需要特殊的判断，所以不用else
            Min = value
       return(Min,Max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试1失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试2失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试3失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试4失败!')
else:
    print('测试成功!')


## 拓展
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

def g():    #生成式generator
    yield 1
    yield 2
    yield 3

#Iterable（可迭代对象，可用For迭代）
print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))  #True
print('Iterable? \'abc\':', isinstance('abc', Iterable))  #True
print('Iterable? 123:', isinstance(123, Iterable))  #False
print('Iterable? g():', isinstance(g(), Iterable))  #True

#iterator（迭代器，可用Next迭代） ,似乎只有生成器可以
print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))  #False
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator)) #True
print('Iterator? \'abc\':', isinstance('abc', Iterator))  #False
print('Iterator? 123:', isinstance(123, Iterator))  #False
print('Iterator? g():', isinstance(g(), Iterator))  #True
    
# iter list:      #用内置函数iter(Iterable)
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')      #next()从0开始计数，第一个next显示第一位
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
