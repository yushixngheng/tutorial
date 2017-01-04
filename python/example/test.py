import subprocess

import os

import time

import win32api

#win32api.Beep(8000,3000)

#os.system('ping www.baidu.com')

#a=subprocess.Popen('ping www.baidu.com',

#                   shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

#b = a.stdout.readlines()

#for i in b:

#    print i



#while True:

#    f = open('D:/Python27/conf.txt', 'r')

#    content = f.read().split('#')

#   if content[0] != '0':

#        win32api.MessageBox(0, content[1], content[2])

 #   time.sleep(5)

win32api.ShellExecute(0, 'open', r'C:\Users\8\Music\冷漠 - 如果离开我你才会幸福.mp3', '', '', 1)



