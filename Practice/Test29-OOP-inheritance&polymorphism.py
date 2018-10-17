
### 继承和多态

## 定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
## 而被继承的class称为基类、父类或超类（Base class、Super class）

class Animal(object):
    def run(self):
        print('Animal is running...')
# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：

class Dog(Animal):
    pass

class Cat(Animal):
    pass


## 继承 的好处是 子类获得了父类的全部功能

## 当父类和子类都存在相同方法时，子类方法会覆盖父类的；运行时，也调用子类的，也就获得了多态
## 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类


## ”开闭“原则

## 调用方只管调用，不管细节，只要确保方法编写正确，不用管原来的代码是如何调用的

## 对扩展开放：允许新增Animal子类；
## 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数


## 静态语言 VS 动态语言

# 对于动态语言来说，则不一定需要传入指定的类型。我们只需要保证传入的对象有类似方法就可以了：

#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，
#走起路来像鸭子”，那它就可以被看做是鸭子。

# Python的“file-like object“就是一种鸭子类型。
# 对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
# 都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。


## 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，
# 也可以把父类不适合的方法覆盖重写。
