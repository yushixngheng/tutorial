#os模块

import os



#获取操作系统平台

print os.name



#获取工作目录

print os.getcwd()



#获取某个目录下的所有文件名

print os.listdir("d:/python27")



#运行一个shell命令

#print os.system("calc")



#删除某个文件

#os.remove("E:/pythondeltest.txt")



#判断一个地方是文件还是文件夹

print os.path.isfile("E:\pythondeltest1.txt")

print os.path.isdir("E:\yu_work")



#把一个路径拆分为目录+文件名的形式

print os.path.split("E:/pythontest/1.txt")

print os.path.split("E:/pythontest")

print os.path.split("E:/pythontest/")

