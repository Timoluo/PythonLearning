### List

## list是一种有序的集合，可以随时添加和删除其中的元素

# 用len()函数可以获得list元素的个数
# 索引是从0开始的,当索引超出了范围时，Python会报一个IndexError越界错误，
# 记得最后一个元素的索引是len(classmates) - 1

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
>>> classmates.append('Adam')
>>> classmates
# ['Michael', 'Bob', 'Tracy', 'Adam']

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
>>> classmates.insert(1, 'Jack')
>>> classmates
#['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

# 要删除list末尾的元素，用pop()方法：
>>> classmates.pop()
#'Adam'
>>> classmates
#['Michael', 'Jack', 'Bob', 'Tracy']
# 要删除指定位置的元素，用pop(i)方法

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
>>> classmates[1] = 'Sarah'
>>> classmates
#['Michael', 'Sarah', 'Tracy']

# list里面的元素的数据类型也可以不同,list元素也可以是另一个list
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组


###Tuple

## tuple 元组，和list非常类似，但是tuple一旦初始化就不能修改

# 获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]
# 没有append()，insert()；也不能赋值成另外的元素 ->  **安全**

#tuple的陷阱：当你定义tuple时，在定义的时候，tuple的元素就必须被确定下来 （类似数组长度一定）
>>> t = (1, 2)
>>> t
#(1, 2)

# *要定义一个只有1个元素的tuple，必须加一个逗号“,”
>>> t = (1,)
>>> t
#(1,)

# 否则，定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号
# 这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1

# 可变的tuple
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
#('a', 'b', ['X', 'Y'])

# tuple的每个元素，*指向永远不变*，变的只是list的元素

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])



