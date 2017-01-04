#远程控制开关机项目

import poplib            ##用来接收读取邮件

import smtplib           ##用来登陆邮件和发送邮件

from email.header import decode_header

from email.mime.text import MIMEText

import email

import time

import sys

import os





#先看模块划分

def guanji():

    #此函数负责发送关机标题(即guan)给邮箱

    sent = smtplib.SMTP("smtp.sina.com")

    sent.login("yushixingheng@sina.com","111111")#这里一定注意，填的是独立密码

    #发送邮件

    #刚才我们已经登陆啦，现在需要设置发送的内容，然后发送即可

    to = ["yushixingheng@sina.com"]

    content = MIMEText("This is a python mail test?")   #设置邮件的具体内容

    content["Subject"] = "guan"                         #设置邮件的主题，标题

    content["From"] = "yushixingheng@sina.com"          #设置邮件从哪里发送

    content["To"] =",".join(to)                         #设置邮件发送到哪里去,可以群发

    #print content["To"] 

    sent.sendmail("yushixingheng@sina.com",to,content.as_string())#实现发送邮件

    sent.close()





def chongqi():

    #此函数负责发送关机重启(即chong)给邮箱

    sent = smtplib.SMTP("smtp.sina.com")

    sent.login("yushixingheng@sina.com","111111")#这里一定注意，填的是独立密码

    #发送邮件

    #刚才我们已经登陆啦，现在需要设置发送的内容，然后发送即可

    to = ["yushixingheng@sina.com"]

    content = MIMEText("")                              #设置邮件的具体内容

    content["Subject"] = "chong"                         #设置邮件的主题，标题

    content["From"] = "yushixingheng@sina.com"          #设置邮件从哪里发送

    content["To"] =",".join(to)                         #设置邮件发送到哪里去,可以群发

    #print content["To"] 

    sent.sendmail("yushixingheng@sina.com",to,content.as_string())#实现发送邮件

    sent.close()





def read():

    #如何读取邮件

    read = poplib.POP3("pop.sina.com")

    read.user("yushixingheng@sina.com")

    read.pass_("6654ws12106xy")

    tongji = read.stat()

    #print tongji#read.stat返回的是邮箱的数量和总自己数

    

    #服务器将返回由参数标识的邮件前0行内容，最后str为一个列表，有三个参数

    str = read.top(tongji[0],0)#返回最近的邮件信息

    #print str  #返回3个参数 [1]对我们有用

    str2 = []



    #其中str[1],也就是说str中的第二个参数为第一封邮件的各种信息,在这里给其进行编码

    for x in str[1]:

        try:

            str2.append(x.decode())

        except:

            try:

                str2.append(x.decode("gbk"))

            except:

                str2.append((x.decode("big5")))



    #这个方法能把String的邮件转换成email.message实例

    #msg是把经过编码的str2转化为可识别的邮件信息，并且每行一个信息，join用来连接字符串

    msg = email.message_from_string("\n".join(str2))

    biaoti = decode_header(msg["subject"])

    #print biaoti

    if biaoti[0][1]:#如果有第二个元素，说明有编码信息

        biaoti2 = biaoti[0][0].decode(biaoti[0][1])

    else:

        biaoti2 = biaoti[0][0]



    #此时成功获取最近一封邮件标题，即biaoti2

    if biaoti2 == "guan":

        return 0

    if biaoti2 == "chong":

        return 1

    read.quit()



def chongzhi():

    #此函数负责发送关机标题(即chongzhi)给邮箱

    sent = smtplib.SMTP("smtp.sina.com")

    sent.login("yushixingheng@sina.com","6654ws12106xy")#这里一定注意，填的是独立密码

    #发送邮件

    #刚才我们已经登陆啦，现在需要设置发送的内容，然后发送即可

    to = ["yushixingheng@sina.com"]

    content = MIMEText("This is a python mail test?")   #设置邮件的具体内容

    content["Subject"] = "reflash"                      #设置邮件的主题，标题

    content["From"] = "yushixingheng@sina.com"          #设置邮件从哪里发送

    content["To"] =",".join(to)                         #设置邮件发送到哪里去,可以群发

    #print content["To"] 

    sent.sendmail("yushixingheng@sina.com",to,content.as_string())#实现发送邮件

    sent.close()





#此函数负责读取邮件中的指令，指令为guan返回0，指令为chong返回1

if __name__=='__main__':#当运行此程序的时候，读取邮件

    while True:

        time.sleep(2)

        if read() == 0:

            os.system('shutdown -s -t 60 -c  "鬼来啦"')

            chongzhi()

            break

        if read() == 1:

            os.system('shutdown -r  -c "我回来啦"')

            chongzhi()

            break







