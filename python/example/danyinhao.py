# -*- coding: cp936 -*-

#单引号

c1 = '2ght'

print c1

c2 = 'It is a "dog" ! '

print c2





#双引号

c3 = "2ght"

print c3

c4 = "It's a dog!"

print c4





#三引号

c5 = '''he

she

my

you are

hello'''

print c5



c6 = """he

she

my

you are

hello"""

print c6





#转义符

print 'It\'s a dog!'

print "hello boy\nhello boy"





#自然字符串

print "hello boy\nhello boy"

print r"hello boy\nhello boy"



print "hello gril\n"*20





#子字符串

#索引运算符从0开始索引

#切片运算符[a:b]是指从第a下标开始到第b-1下标。同样第一位的下标位0

c1 = "jikexueyuan"

c2 = c1[0]

c3 = c1[7]

c4 = c1[:2]

c5 = c1[2:]

c6 = c1[4:7]

print c1

print c2

print c3

print c4

print c5

print c6





#列表

students = ["小明", "小华", "小李", "小娟", "小云"]

print students[3]

students[3] = "小月"

print students[3]





#元组

students = ("小明", "小军", "小强", "小武", "小龙")

print students[1]

#students[1] = "小云"

##print students[3]





#集合

a = set("abcnmaaaaggsng")

b = set("cdfm")

#交集

x = a&b

print x

#并集

y = a|b

print y

#差集

z = a-b

print z

#去除重复元素

new = set(a)

print new

print a





#字典

k = {"姓名":"虞加新", "籍贯":"安徽安庆"}

print k["籍贯"]



#添加字典里面的项目

k["爱好"] = "音乐"

print k["姓名"]

print k["爱好"]











