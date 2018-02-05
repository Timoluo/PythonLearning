### if 语句

## 根据Python的缩进规则，判断后只执行同样缩进的语句
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
# elif是else if的缩写，完全可以有多个elif
# **else 注意不要少写了:

## if语句执行有个特点，它是从上往下判断，
## 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
#'teenager'

# if判断条件还可以简写，比如写：
if x:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False


## 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
# 输入字符串'abc'会报错，因为int()发现一个字符串不是合法的数字，需要捕捉运行期错误


# 小明身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

height = 1.75
weight = 80.5
bmi = float(weight/(height*height))
# bmi=weight/(1.751.75)  #或者bmi=weight/(1.75**2)Python平方求法

# 条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行
if bmi < 18.5:
   print('过轻')
elif bmi<25:
   print('正常')
elif bmi<28:
   print('过重')
elif bmi<32:
   print('肥胖')
else:
   print('严重肥胖')
