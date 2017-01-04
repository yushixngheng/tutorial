#获取极客学院官网前20页课程



import requests

import re

import sys

#reload(sys)

#sys.setdefaultencoding("utf-8")





class spider():

    def __init__(self):

        print u'begin to search。。。'

        

    def getsource(self, url):

        html = requests.get(url)

        html.encoding = "utf-8"

        return html.text



    def changepage(self, url, total_page):

        now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))

        page_group = []

        for i in range(now_page, total_page+1):

            link = re.sub('pageNum=\d+', 'pageNum=%s'%i, url, re.S)

            page_group.append(link)

        return page_group



    def geteveryclass(self, source):

        everyclass = re.findall('(<li deg="".*?</li>)', source, re.S)

        return everyclass



    def getinfo(self, eachclass):

        info = {}

        info['title'] = re.search('target="_blank">(.*?)</a>', eachclass, re.S).groud(1)

        info['content'] = re.search('</h2><p>(.*?)</p>', eachclass, re.S).groud(1)

        timeandlevel = re.findall('<em>(.*?)</p>', eachclass, re.S)

        info['classtime'] = timeandlevel[0]

        info['classlevel'] = timeandlevel[1]

        info['learnnum'] = re.search('"learnnum">(.*?)</em>', eachclass, re.S).groud(1)

        print info['title'] 

        return info

    

    def saveinfo(self, classinfo):

        f = open('info.txt',"a")

        for each in classinfo:

            f.writelines('title:' + each['title'] + '\n')

            f.writelines('content:' + each['content'] + '\n')

            f.writelines('classtime:' + each['classtime'] + '\n')

            f.writelines('classlevel:' + each['classlevel'] + '\n')

            f.writelines('learnnum:' + each['learnnum'] + '\n')

        f.close



if __name__ == '__main__':

    classinfo = []

    url = 'http://www.jikexueyuan.com/course/?pageNum=1'

    jikespider = spider()

    all_links = jikespider.changepage(url, 20)

    for link in all_links:

        #print u'begin web: " + link

        html = jikespider.getsource(link)

        everyclass = jikespider.geteveryclass(html)

        for each in everyclass:

            info = jikespider.getinfo(each)

            classinfo.append(info)

        jikespider.saveinfo(classinfo)

                          

