
### map/reduce

## map()函数接收两个参数，一个是函数，一个是Iterable，
## map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25


# 字符串转化为整数

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

#用lambda进一步后：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


## 测试

#用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
#其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# -*- coding: utf-8 -*-
def normalize(name):  
    return name.title()   #默认把首字母大写，其他小写的函数；Captial只做大写
  pass

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))     #normalize 使字符串都小写
print(L2)


# 编写一个prod()函数，可以接受一个list并利用reduce()求积

# -*- coding: utf-8 -*-
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,map(int,L))  #直接用L也可以,但是出来其实是str
    pass

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

##  rang()  rang(3)=[0,1,2] // range([start], stop[, step])
##  生成一定范围内的数， start: 起始数
##  stop: 上限数，不包括; step: 每个数之间的差



# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    #放在一起计算
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    p = s.rindex('.')    #rindex是倒着数的顺序，用来计算小数点后的位数
    temp = s.replace('.','')
    return (reduce(lambda x,y:x*10 + y, map(lambda x:DIGITS[x], temp)))/pow(10,p)
    pass


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

#分成两部分计算   //缺少小数点是否存在的判断
  a,b =s.split(".")
  print("a=",a,"b=",b)
  int1=reduce(lambda x,y:10*x+y,map(int,a)) 
  int2=reduce(lambda x,y:10*x+y,map(int,b))/pow(10,len(b))
  return int1+int2
  pass
