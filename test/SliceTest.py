#-*-coding:utf-8-*-

def trim(s):
     if s=='':
        return s
     while s[0]== ' ':
        s= s[1:]
        if s=='':     #防止清空成''
          return s   # break
     while s[-1]== ' ':
        s= s[:-1]
        if s=='':      #防止清空成''
          return s    # break
     return s


#测试:
if trim('hello  ')!='hello':
    print('测试1失败!')
elif trim(' hello')!='hello':
    print('测试2失败!')
elif trim(' hello ')!='hello':
    print('测试3失败!')
elif trim('  hellow orld  ')!='hellow orld':
    print('测试4失败!')
elif trim('')!='':
    print('测试5失败!')
elif trim('   ')!='':
    print('测试6失败!')
else:
    print('测试成功!')


# SyntaxError: unindent does not match any outer indentation level

## 由于Tab和Space混用导致的错误
