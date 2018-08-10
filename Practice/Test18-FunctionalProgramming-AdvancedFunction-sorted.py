
### sorted 排序算法

## 排序的核心是比较两元素大小
## 数字可以直接比较；字符串或者dict就需要 函数 sorted来抽象比较过程


#Python内置的sorted()函数就可以对list进行排序：

>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
#sorted()函数也是高阶函数，它还可以接收一个key函数来实现自定义排序，例如按绝对值大小排序：

>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]


## key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
## 默认--根据返回的值，从小到大排序

## 默认情况下，字符串排序是按照ASCII大小比较的，由于'Z' < 'a'，大写Z会排在小写a的前面
##  ['Credit', 'Zoo', 'about', 'bob']

# sorted传入key函数，即可实现忽略大小写的排序：
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']


##练习

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
   return t[0]      #t[0]默认返回tuple中的第一个值，sorted再根据返回的值从小到大排列

L2 = sorted(L, key=by_name)
print(L2)

#再按成绩从高到低排序：
# -*- coding: utf-8 -*-
def by_score(t):
   return -t[1]     #-t[1]先返回value，由于sorted默认升序，用-改变值，偷偷反转顺序

L2 = sorted(L, key=by_score)
print(L2)
