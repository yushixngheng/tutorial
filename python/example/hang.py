#逻辑行和物理行



#以下是3个物理行

print "abc"

print "789"

print "777"



#以下是1个物理行,3个逻辑行

print "abc";print "789";print "777"



#以下是1个逻辑行,3个物理行

print '''I

LOVE

YOU!'''



#行连接

print "hello \

world!!!"





a = 777

#    print a

print a





#如何缩进



#一般情况下，行首应该不留空白

import sys



#缩进的方法有两种，可以按空格，也可以按tab键



#if语句的缩进方法

a = 7

if a > 0:

    print "hello"



#while语句的缩进方法

b = 0

while b < 7:

    print b;

    b += 1;

