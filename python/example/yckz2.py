#-*-coding:utf8-*-

from email.mime.text import MIMEText
from configReader import configReader
#from mccLog import mccLog
import poplib
import smtplib
import re

class mailHelper(object):
    CONFIGPATH = '_config.ini'

    def __init__(self):
        #self.mccLog = mccLog()
        cfReader = configReader(self.CONFIGPATH)
        self.pophost = cfReader.readConfig("Slave", "pophost")
        self.smtphost = cfReader.readConfig("Slave", "smtphost")
        self.port = cfReader.readConfig("Slave", "port")
        self.username = cfReader.readConfig("Slave", "username")
        self.password = cfReader.readConfig("Slave", "password")
        self.bossMail = cfReader.readConfig("Slave", "bossMail")
        self.loginMail()
        #self.configSlaveMail()

    def loginMail(self):
        #self.mccLog.mccWriteLog(u'开始登录邮箱')
        print '开始登录邮箱'
        try:
            self.pp = poplib.POP3_SSL(self.pophost)
            self.pp.set_debuglevel(0)
            self.pp.user(self.username)
            self.pp.pass_(self.password)
            self.pp.list()
            print u'登陆成功!'
            #self.mccLog.mccWriteLog(u'登录邮箱成功。')
        except Exception,e:
            print u'登陆失败！'
            #self.mccLog.mccError(u'登录邮箱失败' + str(e))
            exit()

    def acceptMail(self):
        #self.mccLog.mccWriteLog(u'开始抓取邮件。')
        print '开始抓取邮件。'
        try:
            ret = self.pp.list()
            mailBody = self.pp.retr(len(ret[1]))
           # self.mccLog.mccWriteLog(u'抓取邮件成功。')
            print '抓取邮件成功。'
            return mailBody
        except Exception,e:
            #self.mccLog.mccError(u'抓取邮件失败’ + str(e)')
            print '抓取邮件失败’ + str(e)'
            return None

    def analysisMail(self, mailBody):
        #self.mccLog.mccWriteLog(u'开始抓取subject和发件人')
        print  '开始抓取subject和发件人'
        try:
            subject = re.search("Subject: (.*?)'", str(mailBody[1]).decode("utf-8"),re.S).group(1)
            sender = re.search("x-Sender (.*?)'", str(mailBody[1]).decode("utf-8"),re.S).group(1)

            command = {"subject":sbuject, "sender":sender}
            #self.mccLog.mccWriteLog(u'抓取subject和发件人成功')
            print "抓取subject和发件人成功"
        except Exception, e:                           
            return None
    def configSlaveMail(self):
        print "开始配置发件箱"
        try:
            self.handle = smtplib.SMTP(self.smtphost, self.port)
        except Exceptinon, e:
            return False

    def sendMail(self, subject, receiver, body = "Sucess"):
        msg = MIMEText(body, "plain", "utf-8")#中文需参数"utf-8",单字节字符不需要
        msg["Subject"] = subject
        msg['from'] = self.username
        if receiver == "Slave":
            try:
                self.handle.sendmail(self.username, self.username, msg.as_string)
                return True
            except Exception, e:
                return False
        elif receiver ="Boss"

if __name__ == "__main__":
    mail = mailHelper()
    #body = mail.acceptMail()
    #print mail.analysisMail(body)
    #mail.sendMail("test", "Boss")
        


