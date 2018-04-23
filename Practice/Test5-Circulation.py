### 循环


## Python的循环有两种，一种是for...in循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# Python提供一个range()函数，可以生成一个整数序列，
# 再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

## 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print(acc)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
n = len(L)
while n>0:
   n=n-1          #因为数组从0开始，所以先减一方便取值；此为倒序输出
   print("Hello, %s" % L[n])  


## 在循环中，break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


##也可以通过 continue 语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


## 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多,
## 都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

## 有些时候，如果代码写得有问题，会让程序陷入“死循环”，
## 也就是永远循环下去。这时可以用 Ctrl+C 退出程序，或者强制结束Python进程
