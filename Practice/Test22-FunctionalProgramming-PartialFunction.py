
### 偏函数

## int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

>>> int('12345')
#12345

## 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

>>> int('12345', base=8)
#5349
>>> int('12345', 16)
#74565


#functools.partial就是帮助我们创建一个偏函数的，

>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
#64


# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
# 注意上面的新的int2函数，也可以在函数调用时传入其他值


## 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
## 根据partial接收到第一个函数，将后续参数分别传入*args 或者 **kw中

# 如 int2 = functools.partial(int, base=2)
# 等价于  kw = { 'base': 2 }
#        int('10010', **kw)

# max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，再读取max里的值
# 相当于：args = (10, 5, 6, 7)
#        max(*args)

## 小结
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


## 编外
import functools

def partial(func,part_args):
    def wrapper(extra_args):
        args=list(part_args)
        print("args=",args)
        print("extra_args=",extra_args)
        args.extend(extra_args)  #把extra_args整合到args里面去；
        print("args=",args)
        return func(*args)
    return wrapper

def sub(a,b,c):
    return a+b+c

subb=partial(sub,2,3)
print("subb(4)=",subb(4))


## vim search.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def search_word_in_filename(path, str):
    for x in os.listdir(path):
        if os.path.isfile(x) and str in x:
            print(os.path.join(os.path.abspath(path), x))
        if os.path.isdir(x):
           search_word_in_filename(x, str)

try:
    search_word_in_filename(sys.argv[1], sys.argv[2])
except:
    print('error')
finally:
    print('end')
    
#使用方法：
#./search.py /data/wwwroot/ testname


## 实现partial

class partial:
    def __new__(cls, func, *args, **kwargs):
        if not callable(func):
            raise TypeError("the first argument must be callable")
        self = super().__new__(cls)

        self.func = func
        self.args = args
        self.kwargs = kwargs
        return self

    def __call__(self, *args, **kwargs):
        newkeywords = self.kwargs.copy()
        newkeywords.update(kwargs)
        return self.func(*self.args, *args, **newkeywords)

#使用：

def add(x, y):
    return x + y

inc = partial(add, y=1)
print(inc(41))  # 42


## 接受多个参数的偏函数
import functools

def partial(func,*part_args):
    def wrapper(*extra_args):
        args=list(part_args)
        print("args=",args)
        print("extra_args=",extra_args)
        args.extend(extra_args)  #把extra_args整合到args里面去；extend默认接受iterator
        print("args=",args)
        return func(*args)
    return wrapper

def sub(a,b,c):
    return a+b+c

subb=partial(sub,2,3)
print("subb(4)=",subb(4))

#args= [2, 3]
#extra_args= (4,)
#args= [2, 3, 4]
#subb(4)= 9
