
### 调试


## 查询出错时变量的值是否正确

## 1. print()  直接简单粗暴


## 2. 断言（assert）
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：

# Traceback (most recent call last):
#   ...
# AssertionError: n is zero!


## 启动Python解释器时可以用-O参数来关闭assert.关闭后，你可以把所有的assert语句当成pass来看。
$ python -O err.py
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero


## 3. logging

# logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)  #仅有logging.info智慧输出ZeroDivisionError
print(10 / n)

# INFO:root:n = 0
# Traceback (most recent call last):
#   File "err.py", line 8, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero

## logging允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
## 当我们指定level=INFO时，logging.debug就不起作用了。
## 同理，指定level=WARNING后，debug和info就不起作用了。
## 你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

## logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。


## 4. pdb

# Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

$ python -m pdb err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
#   -> s = '0'
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。
# 输入命令l来查看代码
# 输入命令n可以单步执行代码：
(Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
#   -> n = int(s)
(Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
#   -> print(10 / n)
# 任何时候都可以输入命令p 变量名来查看变量：
# 输入命令q结束调试，退出程序


## 5. pdb.set_trace()

## 只需要import pdb，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，
# 或者用命令c继续运行：

$ python err.py 
# > /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
#  -> print(10 / n)
(Pdb) p n
# 0
(Pdb) c
# Traceback (most recent call last):
#   File "err.py", line 7, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero


## 6.IDE

# 比较好的Python IDE有：
# Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
# PyCharm：http://www.jetbrains.com/pycharm/
# Eclipse加上pydev插件也可以调试Python程序。

## 小结
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

