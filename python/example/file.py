#文件的操作

fc=open("E:/pythontest/10.txt", "r+")

#fc=file("E:/pythontest/11.txt", "w")

#fc=file("E:/pythontest/12.txt", "w")

#t=fc.read()

#t=fc.write("test")

t=fc.readline()

print t

fc.close()



