
###  返回函数

## 函数作为返回值

#实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#但若不需要立刻求和，在后面代码中，根据需要再计算时可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

## 当我们调用lazy_sum()时，返回的不是求和结果，而是求和函数；
## 调用被赋值的函数时，才真正计算值


# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
# f1()和f2()的调用结果互不影响


##  闭包

## 内部函数可以引用外部函数的参数和局部变量，当外部返回内部函数时，
## 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”

# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
#f1()、f2()、f3()全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
#等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

#个人理解： 返回的是三个i*i，此时i指向3，所以均为9

###  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

## 解决方法：再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
##      已绑定到函数参数的值不变：

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

#个人理解： 多包一层函数，并将循环后置，确保了内层函数返回不会被i影响

## 练习

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
# -*- coding: utf-8 -*-

def createCounter():
      x = 0
    def counter():
        nonlocal x                  #nonlocal 用于修改最外层的非局部变量
        x = x + 1
        return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

## 想要对返回函数隔离，就用闭包外层套函数；
## 想要返回内部迭代的值去修改外部的int/str，就用nolocal定义；list/dict则不用

#在闭包中不能修改外部作用域的局部变量，所以在外层函数设置局部变量，到内层函数再赋值返回会抛出错误：
#UnboundLocalError: local variable 'n' referenced before assignment
    
#1.容器法，将变量设置为一个容器，通过下标来修改

def f():
    s=[0]
    def f1():
        s[0]=s[0]+1
        return s[0]
    return f1
c=f()
print(c(),c(),c())>>>1,2,3
#这里用list是因为修改string或int的全局变量会需要在函数内再申明一次；除非是nolocal
#而list或者dict不会产生是新建还是修改的歧义，可直接修改、不用申明

#2.nonlocal，适用于嵌套内部函数修改外部函数局部变量

def f():
    n=0
    def f2():
        nonlocal n
        n=n+1
        return n
    return f2
c=f()
print(c(),c(),c())>>>1,2,3

#3.global，适用于函数内部修改全局变量
n=0

def f():
    def f2():
        global n
        n=n+1
        return n
    return f2
c=f()
print(c(),c(),c())

#4.生成器，返回递增整数数列生成器

def f():
    def f1():
        n=1
        while True:
            yield n
            n=n+1
    it = f1()
    def f2():
        return next(it)
    return f2
c=f()
print(c(),c(),c())
#这个方法很精妙，将前面的知识点串联起来了

## nolocal，global的变量都可修改外部的值；
## 生成器只能影响同级的，但由于返回的是一列数，可直接用next调用下个值
