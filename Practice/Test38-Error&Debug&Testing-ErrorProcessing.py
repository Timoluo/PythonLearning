
### 错误处理

## 我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。
## Python的pdb可以让我们以单步方式执行代码。

## 高级语言通常都内置了一套try...except...finally...的错误处理机制


## try

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，
# 如果有finally语句块，则执行finally语句块，至此，执行完毕。

## 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

## Python的错误其实也是class，所有的错误类型都继承自BaseException,
#  所以需要注意用except捕获异常时，不要用过大的Exception

# 常见的错误类型和继承关系看这里：
## https://docs.python.org/3/library/exceptions.html#exception-hierarchy


## 调用栈

## 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
##  出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

$ python3 err.py
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero


## 记录错误

# Python内置的logging模块可以非常容易地记录错误信息：
#err_logging.py
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


## 抛出错误

# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，
# 而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 要抛出错误，先根据需要，可以定义一个错误的class，选择好继承关系后，用raise语句抛出错误的实例：

# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
# 定义我们自己的错误类型，尽量选择Python已有的内置的错误类型（比如ValueError，TypeError）

# err_reraise.py
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

# 处理错误最恰当的方式是继续往上抛；
# raise语句如果不带参数，就会把当前错误原样抛出；
# 在except中raise一个Error，还可以吧一种类型的的错误转化成另一种
# 只要是合理的转换逻辑就可以，但决不应该转换成毫不相干的Error


## 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：

# -*- coding: utf-8 -*-
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

# Traceback (most recent call last):
#   File "/usercode/file.py", line 17, in <module>
#     main()
#   File "/usercode/file.py", line 14, in main
#     r = calc('99 + 88 + 7.6')
#   File "/usercode/file.py", line 9, in calc
#     return reduce(lambda acc, x: acc + x, ns)
#   File "/usercode/file.py", line 4, in str2num
#     return int(s)
# ValueError: invalid literal for int() with base 10: ' 7.6'

##修改后

from functools import reduce
import re

def str2num(s):
    if re.search('^\s*\d+\s*$', s):  # .strip()也相当于trim
       return int(s)
    else:
       raise ValueError("invalid value %s can't be transfer into integer" % s)

def calc(exp):
    ss = exp.split('+')
    try:
        ns = map(str2num, ss)
    except ValueError as e:
        print("invalid value: %s " % s)
        raise
    else:
        return reduce(lambda acc, x: acc + x, ns)
    finally:
        print("Ending calculation")

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
    
main()

# Ending calculation
# 100 + 200 + 345 = 645
# Ending calculation

# Traceback (most recent call last):
#   File "/usercode/file.py", line 30, in <module>
#     main()
#   File "/usercode/file.py", line 26, in main
#     r = calc('99 + 88 + 7.6')
#   File "/usercode/file.py", line 19, in calc
#     return reduce(lambda acc, x: acc + x, ns)
#   File "/usercode/file.py", line 8, in str2num
#     raise ValueError("invalid value %s can't be transfer into integer" % s)
# ValueError: invalid value  7.6 can't be transfer into integer

def str2num(s):
isFlo = s.find('.')
    if isFlo == -1:
        return int(s)
    else:
        return float(s)
