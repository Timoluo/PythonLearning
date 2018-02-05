
## 编码与反编码 ASCII<<Gb2312<<UTF-8

>>> 'ABC'.encode('ascii')
#  b'ABC'
>>> '中文'.encode('utf-8')
#  b'\xe4\xb8\xad\xe6\x96\x87'

>>> b'ABC'.decode('ascii')
# 'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中文'

#如果bytes中包含无法解码的字节，decode()方法会报错,可以传入errors='ignore'忽略错误的字节
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# '中'


## 字节数的计算

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
>> len(b'ABC')
# 3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
# 6
>>> len('中文'.encode('utf-8'))
# 6


## 格式化字符串

# 占位符	替换内容  格式化方式和C语言一致
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

>>> 'Hello, %s' % 'world'
# 'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# 'Hi, Michael, you have $1000000.'

>>>print('%2d-\\%02d %%' % (3, 1))
>>>print('%.2f' % 3.1415926)
# 3-\01 % 
# 3.14                            %只能用%转义，而不能用\

# %s永远起作用，它会把任何数据类型转换为字符串
>>> 'Age: %s. Gender: %s' % (25, True)
# 'Age: 25. Gender: True'

#  使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 'Hello, 小明, 成绩提升了 17.1%'


##小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
S1=72
S2=85
f = (S2-S1)/S1*100
print('The improvement percentage is %.1f %%' % f)

# The improvement percentage is 18.1 %

n=input('what\'s your name:')
s1=input('请输入去年的成绩：')
s2=input('请输入今年的成绩：')
t=(float(s2)-float(s1))/float(s1)*100
if t>0 :
    print('恭喜%s,你的成绩提高了%.1f%%'%(n,t))
else :
    t=abs(t)
    print('很遗憾%s,你的成绩降低了%.1f%%'%(n,t))
