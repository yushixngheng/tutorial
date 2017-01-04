#lambda

#1 格式： lambda 参数：表达式

lambda x:x+3



a=lambda x:x+3

a(1)

print a(1)

print a(27)





#2

b=lambda x,y,z:x+y

c=lambda x,y,z:x+y-z

#b(1)

print b(1,2,3)

print c(1,2,3)



#上面b用到了2个参数，c用到了3个参数。在传递值的时候

#b不可以给2个参数，声明了多少个参数，就得给多少个参数，不管是否用到

#print b(1,2) 和 print b(1)是错误的



#3

def function(t):

    return lambda x:x+t

d1=function(10) #function(t)=lambda x:x+t d1(10)=function(10)=lambda x:x+10

print d1(7)





def m():

    return lambda s:s*3

k=m()

print k("hello")

#print m("hello")

print m()("hi")

