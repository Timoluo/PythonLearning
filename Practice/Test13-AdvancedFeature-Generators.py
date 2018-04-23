
### 生成器

## 列表元素可以按照某种算法推算出来，可以在循环的过程中不断推算出后续的元素
## 这样就不必创建完整的list，从而节省大量的内存空间。
## 在Python中，这种一边循环一边计算的机制，称为生成器：generator


## generator实时生成数据，只能被迭代一次，不可再用for..in..获取其中的数据
## 当你调用这个函数的时候，函数内部的代码并不立马执行，生成器产生值的时候也是如此


## 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。


# 我们可以直接打印出list的每一个元素，
# 如果要一个一个打印generator出来，可以通过next()函数获得generator的下一个返回值：

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误。

## 正确的方法是使用for循环，因为generator也是可迭代对象：
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
... 

## 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b  #t=(a,b)=(b,a+b)
        n = n + 1
    return 'done'

# 注意，赋值语句：  a, b = b, a + b  相当于：

t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]

## 不必显式写出临时变量t就可以赋值。


#要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：
## 生成器内部没有定义yield 关键字，那么这个生成器被认为成空的

>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>


## 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
## 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
## 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
## 当你调用这个函数的时候，函数内部的代码并不立马执行，生成器产生值的时候也是如此


# 举个简单的例子，定义一个generator，依次返回数字1，3，5：

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：

>>> o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# 在执行过程中，遇到yield就中断，下次又继续执行。我们在循环过程中不断调用yield，就会不断中断。
# 当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。


## 用for循环调用generator时，发现拿不到generator的return语句的返回值。
## 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...

## 练习

# 杨辉三角定义如下：

#          1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：

# -*- coding: utf-8 -*-

def triangles():
        ret = [1]
      while True:
         pre = ret[:]
         yield pre      #L[:],浅copy，除了可变部分，其他部分都不随源值改变 
         for i in range(1, len(ret)):       #输出ret的下面t值会不断改变
              ret[i] =  pre[i] + pre[i - 1]
         ret.append(1)      #用迭代方式加入队尾

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

## 简单方法，去边、只考虑小三角
l = [1]
while 1:
    yield l
    l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1]


## 原方法，只适合list般直接输出；ret值会不断变化，把原来的ret值覆盖
  ret = [1]
   while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1] 
        ret.append(1)
        pre = ret[:]
        print('ret[:]',ret[:])



## 在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
## 普通函数调用直接返回结果，generator函数的“调用”实际返回一个generator对象。
        

### 对象的引用，浅拷贝，深拷贝的区别

import copy
l = [1, 2, 3, [4, 5]]
l1 = l
l2 = l[:]
l3 = copy.deepcopy(l)

print 'l:%d, l1:%d, l2:%d, l3:%d' % (id(l), id(l1), id(l2), id(l3))
# 输出: l:39121992, l1:39121992, l2:39142344, l3:39142216

l3[3][0] = 6
print l
# 输出: [1, 2, 3, [4, 5]]

l2[3][0] = 6
print l
# 输出: [1, 2, 3, [6, 5]]

# l1引用了l，他们是同一个对象，只是变量名不一样，可理解为l1是l的另外一个名字。
# 所以他们打印的id都一样，修改了l1里的东西，其实也就是在修改l。

# l2和l3分别是浅拷贝和深拷贝了l对象，l2和l3都是新的对象，所以他们都有新的id。
# 修改他们的非可变对象（如数字，字符串，元组）时，不会影响到l。

## 深拷贝和浅拷贝区别：浅拷贝中可变对象(如列表，字典类型)仍是引用的原对象l中的对象,
## 所以修改了浅拷贝中的[4, 5]， l也受影响了；但是修改深拷贝中的[4, 5]， l未受影响，
## 因为深拷贝中可变对象也是新拷贝的。
        
