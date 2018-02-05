Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #练习

#请打印出以下变量的值：

#!/usr/bin/env python3    #第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
## -*- coding: utf-8 -*-   #第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码  
#n = 123
#f = 456.789
#s1 = 'Hello, world'
#s2 = 'Hello, \'Adam\''
#s3 = r'Hello, "Bart"'
#s4 = r'''Hello,
#Lisa!'''
>>> 
>>> n = 123
f = 456.789
print(r'# -*- coding: utf-8 -*-')
print('n','=',n,'=123')
print('f','=',f,'=456.789')
print('s1','=','\'Hello, world\'')
print('s2','=','\'Hello, \\\'Adam\\\'\'')
print('s3','=','r\\\'Hello,\"Bart\"\'')
print('s4','=','''r\'\'\'Hello,
Lisa\!\'\'\'''')


n=123
print('n =',n)
f=456.789
print('f =',f)
s1="'Hello, world'"
print('s1 =',s1)
s2="'Hello, \'Adam\''"
print('s2 =',s2)
s3='r\'Hello, "Bart"\''
print('s3 =',s3)
s4="r\'''Hello,\nLisa!'''"
print('s4 =',s4)
