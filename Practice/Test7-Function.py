### Function


## 1.Call Function

#求圆面积，每次要用s = 3.14 * x * x，写成更有意义的函数调用s = area_of_circle(x)，
#而函数area_of_circle本身只需要写一次，就可以多次调用

# 抽象

# 100
# ∑n
# n=1


## 2. Define Function

# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
#99

## 一旦执行到return时，函数就执行完毕，并将结果返回
## 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
## return None可以简写为return

## 交互环境中定义函数时，注意Python会出现...的提示。
## 函数定义结束后需要按两次回车重新回到>>>提示符

# >>> def my_abs(x):                                      │
#│...     if x >= 0:                                      │
#│...         return x                                    │
#│...     else:                                           │
#│...         return -x                                   │
#│...                                                     │
#│>>> my_abs(-9)                                          │
#│9                                                       │


# 把my_abs()的函数保存为abstest.py文件了，在该文件的当前目录下启动Python解释器，
##  用"from abstest import my_abs"来导入my_abs()函数，
##  **注意abstest是文件名（不含.py扩展名）

# >>> from abstest import my_abs                          │
#│>>> my_abs(-9)                                          │
#│9                                                       │
#│>>> _                                                   │


## 定义一个什么事也不做的空函数，可以用pass语句：

def nop():
    pass
# 实际上pass可以用来作为占位符,可以让代码先运行起来
# pass还可以用在其他语句里，比如：
if age >= 18:
    pass
#缺少了pass，代码运行就会有语法错误


## check parameter

# 调用函数时，如果参数个数不对,会抛出TypeError
# 如果参数类型不对，内置函数 和 自定义未检查参数的函数 报错会有差别
#TypeError: unorderable types: str() >= int()  # *未检查

#TypeError: bad operand type for abs(): 'str'  # *内置函数

## 检查参数，只允许int和float 数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


## return mutiple values

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 但其实这是个假象，返回的是一个值，是一个（nx，ny）的tuple。
# 返回tuple可以省略括号；多个变量可以同时接受一个tuple，按位置赋值


##Practice

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。

# 提示：计算平方根可以调用math.sqrt()函数：
>>> import math
>>> math.sqrt(2)
# 1.4142135623730951

# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):

  if not isinstance(a, (int, float)):
        raise TypeError('bad operand type:The type of "a" is not int or float')
  if not isinstance(b, (int, float)):
        raise TypeError('bad operand type:The type of "b" is not int or float')
  if not isinstance(c, (int, float)):
        raise TypeError('bad operand type:The type of "c" is not int or float')
  if a == 0:
      if b==0:
          if c==0:
              print('Countless Results')
          else:
              print('No results')
      else:
          return -c/b
  if b*b-4*a*c>0:
      #var sq as float  ## 不能强制定义类型 好坑爹
      sq=math.sqrt(b*b-4*a*c)
      return (sq-b)/(2*a),(-sq-b)/(2*a)
  else:
     print("The Function have no real results")

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


## Better Example:

import math

def quadratic(a, b, c):
    L = [a, b, c]
    for i in L:
        if not isinstance(i, int):
            raise TypeError("bad operand type")
    num1 = math.pow(b, 2) - 4 * a * c
    if num1 < 0:
        return
    elif num1 == 0:
        res = (-b)/(2*a)
        return res
    else:
        num2 = math.sqrt(num1)
        res1 = (-b + num2)/(2*a)
        res2 = (-b - num2)/(2*a)
        return res1, res2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
