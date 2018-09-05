
### 装饰器

## 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
## decorator就是一个返回函数的高阶函数

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#因为log是一个decorator，接受函数作为参数，并返回函数。需借助@的语法，将其置于函数定义处
@log
def now():
    print('2015-3-25')

#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
>>> now()
#call now():
#2015-3-25

#把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)

#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
#只是同名的now变量指向了新的函数，于是调用now()将执行在log()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
#在wrapper()函数内，首先打印日志，再紧接着调用原始函数。


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#和两层嵌套相比
>>> now = log('execute')(now)

## 但是这样调用装饰器会改变原函数的一些固有属性，如now._name_;需要调用functools.wraps

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

    # 或者针对带参数的decorator：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


## 练习
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

# -*- coding: utf-8 -*-
def metric(fn):
#    print('%s executed in %s ms' % (fn.__name__, 10.24))
#    return fn
    @functools.wraps(fn)
    def func1(*args,**kw):
        startTime = time.time()
        result = fn(*args, **kw)
        useTime = time.time() - startTime
        print('%s executed in %s ms' % (fn.__name__, useTime))
        return fn(*args,**kw)                       
    return func1

#测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


## 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
## OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
## 直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。


## 高级

    def metric(*text):    #可变参数可接受0到多个参数(多个组合成tuple/list)
    def decorator(fn):
        # 交换 __name__ 属性
        @functools.wraps(fn)
        def wapper(*args, **kw):      #0，1 format传参 || 列表达式
            print('{}: {}'.format(text if text else 'call', fn.__name__))
            start = time.time()
            re = fn(*args, **kw)
            end = time.time()
            print('运行时间：{} s'.format(end - start))
            return re

        return wapper

    if isinstance(text[0], str):      #若text为字符串则输出，返回无参
        text = text[0]
        return decorator
    else:
        tmp = text[0]
        text = ''
        return decorator(tmp)
