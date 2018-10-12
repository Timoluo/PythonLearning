
### 使用元类

## type()

## 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

# hello.py模块：
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
# 引入hello模块：
>>> from hello import Hello
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class 'hello.Hello'>  # hello模块下的Hello函数

# type()函数可以查看一个类型或变量的类型，Hello是一个class，
# 它的类型就是type，而h是一个实例，它的类型就是class Hello。

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，可以通过type()函数创建出Hello类
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class '__main__.Hello'>


##要创建一个class对象，type()函数依次传入3个参数：

## 1. class的名称；
## 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
## 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助工具生成字节码实现动态编译


## metaclass

# 一般定义了类以后，就可以根据这个类创建出实例，    所以：先定义类，然后创建实例。
# 要想创建出类呢，那就必须根据metaclass创建出类， 所以：先定义metaclass，然后创建类。
##      连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# metaclass允许你创建类或者修改类。  你可以把类看成是metaclass创建出来的“实例”。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value) #把append的方式赋予add
        return type.__new__(cls, name, bases, attrs)  #返回添加了add方法的attr

class MyList(list, metaclass=ListMetaclass):
    pass

# 当传入关键字参数metaclass时，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，我们可以修改类的定义，
#比如，加上新的方法，然后，返回修改后的定义。

## __new__()方法接收到的参数依次是：
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

## ORM就是需要通过metaclass动态修改类定义的典型例子
## ORM全称“Object Relational Mapping”，即对象-关系映射，
# 就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，
#剩下的魔术方法比如save()全部由metaclass自动完成。
#虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。


# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name) #返回类名与field值
    
# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 下一步，就是编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v       #打印并保存映射
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 以及基类Model：
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

#输出：
#SQL: insert into User (password,email,username,id) values (?,?,?,?)
#ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]

# 在ModelMetaclass中，一共做了几件事情：
# 排除掉对Model类的修改；
# 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，
#    就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
#    否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
# 把表名保存到__table__中，这里简化为表名默认为类名。

## 小结
# metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。
# metaclass可以通过python解释器自发的向上层方法查找隐式地继承到子类，但子类自己却感觉不到
## 元类大多用来：
#  1)   拦截类的创建
#  2)   修改类
#  3)   返回修改之后的类


## 补充

# 当通过class声明去创建类的时候，Python自动在最后加上了type(name, supers, attrs)去生成类。
# 同时type的call属性又调用了如下两种方法：
# (1) type.new(typeclass, name, supers, attrs)
# (2) type.init(class, name, supers, attrs)
#  (1) 可以返回一个新的类，(2) 可以将新类初始化。
# 我们可以通过如下的方式在元类Meta中重载type的方法来管理类的创建，其实也可以重载type的call方法。

# https://www.jianshu.com/p/21857172fb3d

# https://segmentfault.com/a/1190000007460181

# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

# http://blog.jobbole.com/21351/
