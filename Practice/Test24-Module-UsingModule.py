
### 使用模块

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


## sys模块有一个argv变量，用list存储了命令行的所有参数。交互模式中需对argv提前赋值

# argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
# 运行python3 hello.py获得的sys.argv就是['hello.py'];
# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。

## 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#  而如果在其他地方导入该hello模块时，if判断将失败，
#  因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试

## 而在交互模式中，因为没有执行 test(),不会打印语句，调用hello.test()时，才会打印
## 当调用一个module时，此时的__name__取值为模块的名字，所以if判断为假，不执行后续代码，
## 可以用来过滤 被调用后产生的多余结果


## 作用域

## 在Python中，是通过_前缀来实现跨作用域的。

## 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
## 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，
# 比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以
# 用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

## 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，
#  比如_abc，__abc等；
## 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
# 因为Python没有方法可以完全限制访问private函数/变量，
# 但从编程习惯上不应引用private函数或变量。

## 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。



## import abc
#  importlib.reload(module) 更新导入模块


## import mycompany.hello   或 from mycompany import hello
#  mycompany.hello.nihao()          #导入放在mycompany目录下的hello模块


    
