
### 定制类

## __str__

# 只需要定义好__str__()方法，print的时候就可以返回一个好看的字符串了：

>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...     def __str__(self):
...         return 'Student object (name: %s)' % self.name
...
>>> print(Student('Michael'))
Student object (name: Michael)

# 直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。

# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的
# 可以直接 __repr__=__str__


## __iter__

## 实现__iter__(),返回一个迭代循环对象，类似于list或tuple，然后调用__next()__拿到下一个
## 直到遇到StopIteration错误，退出
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值


## __getitem__

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

# 像list一样切片会报错，要判断__getitem__()接受的参数是一个int，还是一个切片对象slice
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 还可以把对象看成dict，可以用__getitem__(),__setitem__(),__delitem__()来表现

## 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
## 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


## __getattr__

# 要避免调用属性不存在的错误，可以用__getattr__(),动态返回一个属性

# 只有在没有找到属性的情况下，才调用__getattr__
# 任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

## 这样的动态调用，完全针对完全动态的情况做调用，例如下列API地址的获取
    class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

>>> Chain().status.user.timeline.list
# '/status/user/timeline/list'
# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

# 还有些REST API会把参数放到URL中，比如GitHub的API：
GET /users/:user/repos

#调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
Chain().users('michael').repos


## __call__

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

>>> s = Student('Michael')
>>> s() # self参数不要传入
# My name is Michael.

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
# 因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
# 比如函数和我们上面定义的带有__call__()的类实例：

>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

## 小结
# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。

    
