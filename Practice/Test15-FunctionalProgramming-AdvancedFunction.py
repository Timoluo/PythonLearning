

###函数式编程


# 函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，
# 就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。

# 函数就是面向过程的程序设计的基本单元。


## 纯粹的函数式编程语言抽象程度很高，编写的函数没有变量，输出确定。
## 函数式编程还有一个特点： 允许把函数本身作为参数传入另一个函数，还允许返回一个函数


## 变量指向函数

>>> f = abs
>>> f
<built-in function abs>
##结论：函数本身也可以赋值给变量，即：变量可以指向函数


## 函数名也是变量

>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

# 注：由于abs函数实际上是定义在import builtins模块中的，
# 所以要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10


## 传入函数

# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs)) #11

