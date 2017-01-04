#Python异常的处理

#使用try...except语句，假如try出现了某种异常，则执行except下面的语句

try:

    print i

except NameError:   #这里一定要指明异常类型

    i = 9

    i += 10

    print "刚才i没定义，处理异常之后，i的值为:" + str(i)





#处理多种异常

try:

    print i+j

except NameError:

    i=j=0

    print "刚刚i和j没有进行初始化数据，现在我们将其都初始化位0，结果是:"

    print i+j

except TypeError:

    print "刚刚i和j类型对应不上，我们转换一下类型即可处理异常，处理后：结果是" \

          +str(i)+str(j)





#异常的引发

#1/用raise引发一个系统的错误类

#i = 8

#print i

#if i>7:

#    print 9

#    raise NameError

#    print 10





#2/自定义一个异常并用raise引发

class RhhError(Exception):#按照命名规范，以Error结尾，

                            #并且自定义异常需要继承exception类

    def __init__(self):

        Exception.__init__(self)

try:

    i = 8

    if i > 7:

        raise RhhError

except RhhError, a:

    print "RhhError:错了就是错了"





#3/自定义一个多参数的异常并用raise引发

class HhhError(Exception):

    def __init__(self, x, y):

        Exception.__init__(self, x, y)

        self.x = x

        self.y = y

try:

    x = 3

    y = 1

    if x > 2 or x + y > 7:

        raise HhhError(x, y)

except HhhError:

    print "HhhError:x必须小于2且x+y小于等于7，现在的x是"+str(x)+"现在的y是" +str(y)



        

    

