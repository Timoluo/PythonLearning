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

##  ***定义默认参数要牢记一点：默认参数必须指向不变对象！ 否则自动叠加

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


## 关键字参数

# 许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict



