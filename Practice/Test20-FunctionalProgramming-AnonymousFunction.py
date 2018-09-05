
### 匿名函数

#Python中，对匿名函数提供了有限支持
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

## 关键字lambda表示匿名函数，冒号前面的x表示函数参数
## 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
## 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：


>>> f = lambda x: x * x
>>> f
# <function <lambda> at 0x101c6ef28>
>>> f(5)
# 25


## 练习

#用匿名函数改造下面代码

# -*- coding:utf-8 -*-
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)


print(list(filter(lambda n: n%2==1,range(1,20))))

## 他人心得：lambda匿名函数的返回值与函数参数（输入）无关，只与：后面表达式的结果有关
