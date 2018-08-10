

### filter

## filter()函数用于过滤序列

# filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]


##删空字符串
def not_empty(s):
    return s and s.strip()    #用与非判断是否为空，strip应该用于去空

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']


## filter()函数返回的是一个Iterator，也就是一个惰性序列，
## 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list


##用filter求素数

def _odd_iter():            #用奇数列排除偶数，缩小范围
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):                #代表 取出不能被之前的数整除的数
    return lambda x: x % n > 0        #x之后会由it列的数代替

def primes():
    yield 2          # 取第一个素数2
    it = _odd_iter() # 初始奇数序列
    while True:                             #取出it中的n，不断筛选it后面的数
        n = next(it) # 返回序列的第一个数     
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

##练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]   #[::-1]指的是从尾到头一次取值，相当于翻转了字符串

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    

# filter()的作用是从一个序列中筛出符合条件的元素。
# 由于filter()使用了惰性计算，所以只有在取filter()结果的时候，
# 才会真正筛选并每次返回下一个筛出的元素。
        
