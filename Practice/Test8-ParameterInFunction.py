###  函数的参数

## Python的函数定义灵活度非常大。
## 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数

# 位置函数

def power(x):
    return x * x
# 要计算x4、x5…，就要把power(x)修改为power(x, n)，用来计算x^n
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

## x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序*依次*赋给参数x和n


# 默认函数

# 新的power(x, n)函数定义没有问题，但旧的函数调用函数power()缺少了一个位置参数n
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 当我们调用power(5)时，相当于调用power(5, 2)

# 设置默认参数时，有几点要注意：

## 一是必选参数在前，默认参数在后，否则Python的解释器会报错；

# 二是如何设置默认参数。
## 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 默认函数的好处是能降低调用函数的难度，只有与默认参数信息不符的值才需要提供额外的信息

# 当不按顺序提供部分默认参数时，*需要把参数名写上。
#比如调用enroll('Adam', 'M', city='Tianjin')

##  ***定义默认参数要牢记一点：默认参数必须指向不变对象！ 否则自动叠加（!!List[]）

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。


## 可变参数

#可变参数就是传入的参数个数是可变的
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#但是调用的时候，需要先组装出一个list或tuple：

>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
#如果利用可变参数，调用函数的方式可以简化成这样：

>>> calc(1, 2, 3)
14
>>> calc(1, 3, 5, 7)
84
#所以，我们把函数的参数改为可变参数：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

## list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
>>> nums = [1, 2, 3]
>>> calc(*nums)
14


## 关键字参数  ——不限制关键字，用于扩展

# 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 它可以扩展函数，他将非必要的参数复制一个dict传给对应**kw参数，而不会影响本身的dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
# >>> person('Adam', 45, **extra)


## 命名关键字参数    ——限制关键字，用于圈定

# 要限制关键字参数的名字，可以用命名关键字参数，要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 例如，只接收city和job作为关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

# 如果函数定义中已经有了一个可变参数*args，后面的命名关键字参数就不再需要一个特殊分隔符*了
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名,会报错（位置参数过多）
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer                #命名关键字参数可以用缺省值来简化

##如果没有可变参数，就必须加一个*作为特殊分隔符。否则将视作位置函数。


## 函数组合

## 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 任意函数，都可以通过类似func(*args, **kw)的形式调用

>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)      # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}  
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

## 使用太多组合会使函数接口的可理解性很差


#  Practice

# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

# -*- coding: utf-8 -*-

# def product(x, y):
#     return x * y     //原函数

def product(*args):
  if len(args) == 0:
     return x       # //x未定义，为None.    // raise TypeError("Empty tuple!")
  if len(args)>0:
      y=1
      for i in args:
         y= y * i
      return y

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


## 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

#要注意定义可变参数和关键字参数的语法：

## *args是可变参数，args接收的是一个tuple； **kw是关键字参数，kw接收的是一个dict。
## 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，
        #再通过*args传入：func(*(1, 2, 3))；

## 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，
# 再通过**kw传入：func(**{'a': 1, 'b': 2})。

## 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

## 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

## 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。













