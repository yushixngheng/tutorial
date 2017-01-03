# Yum 手册

## 1.什么是Yum

Yum（Yellow dog Updater, Modified）是一个基于RPM包管理的字符前端软件包管理器。能够从指定的服务器自动下载RPM包并且安装，可以处理依赖性关系，并且一次安装所有依赖的软件包，无须繁琐地一次次下载、安装。被Yellow Dog Linux本身，以及Fedora、Red Hat Enterprise Linux采用。


## 2.Yum配置
Yum的配置分为两个部分: **main** 、**repository**

* main 定义了全局配置，整个Yum配置应该只有一个main，常位于/etc/yum.conf中
* repository 定义了每个源的具体配置，可以有一个或者多个。常位于/etc/yum.repo.d目录

## 3. *.repo文件详解
repo文件是Fedora中yum源（软件仓库）的配置文件，通常一个repo文件定义了一个或者多个软件仓库的细节内容，例如我们将从哪里下载需要安装或者升级的软件包，repo文件中的设置内容将被yum读取和应用！

我们以一份系统自带的epel.repo文件做为实例来探讨（#号后面是我加的注释）： 
![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/epel.repo.png)

[fedora]      #方括号里面的是软件源的名称，将被yum取得并识别  
name=Fedora $releasever - $basearch   #这里也定义了软件仓库的名称，通常是为了方便阅读配置文件，一般没什么作用，$releasever变量定义了发行版本，通常是8，9，10等数字，$basearch变量定义了系统的架构，可以是i386、x86_64、ppc等值，这两个变量根据当前系统的版本架构不同而有不同的取值，这可以方便yum升级的时候选择适合当前系统的软件包，以下同……  
baseurl=http://download.fedoraproject.org/pub/epel/6/$basearch
#这一行的意思是指定一个baseurl（源的镜像服务器地址）  
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=$basearch
#上面的这一行是指定一个镜像服务器的地址列表，通常是开启的，本例中加了注释符号禁用了，我们可以试试，将$basearch替换成自己对应的版本和架构，例如i386，在浏览器中打开，我们就能看到一长串镜可用的镜像服务器地址列表。
选择自己访问速度较快的镜像服务器地址复制并粘贴到repo文件中，我们就能获得较快的更新速度了，格式如下baseurl所示：  
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/6/x86_64/  
failovermethod=priority　　#failovermethod 有两个值可以选择，priority是默认值，表示从列出的baseurl中顺序选择镜像服务器地址，roundrobin表示在列出的服务器中随机选择
enabled=1 #这个选项表示这个repo中定义的源是启用的，0为禁用  
gpgcheck=1 #这个选项表示这个repo中下载的rpm将进行gpg的校验，已确定rpm包的来源是有效和安全的
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6 #定义用于校验的gpg密钥

### 4.CentOS搭建本地yum源
UM主要用于自动升级、安装\移除rpm软件包，它能自动查找并解决rpm包之间的依赖关系，要成功的使用YUM工具更新系统和软件，需要有一个包含各种rpm软件包的repository（软件仓库），提供软件仓库的服务器习惯上成为“源”服务器。网络上有大量的源服务器，但是，由于受到网络连接速度、带宽的限制，导致软件安装耗时过长甚至失败。特别是当有大量服务器大量软件包需要升级时，更新的缓慢程序令人难以忍受。

相比较而言，本地YUM源服务器最大优点在局域网的快速网络连接和稳定性。有了局域网中的YUM源服务器，即便在Internet连接中断的情况下，也不会影响其他YUM客户端的软件升级和安装。  
下面就介绍下 本地yum源的搭建。
#### 4.1启动httpd服务（一般httpd服务已经安装）

取一台 CentOS操作系统的机器作为源服务器。启动服务器的httpd 服务：service httpd start

可查看配置文件: /etc/httpd/conf/httpd.conf  了解httpd相关配置信息

这里我们配置的文档根目录为：/var/www/html/ 端口: Listen 80

确认服务启动，浏览器访问： http://localhost:80 出现如下apache页面（如果从其他机器访问，请先关闭防火墙：service iptables stop ）
#### 4.2 安装 createrepo 工具
createrepo是linux下的创建仓库的软件包。  
在机器联网的情况下可直接安装：  
yum install createrepo   

#### 4.3 创建本地yum库
初始化repodata信息:  
createrepo -pdo  /var/www/html /var/www/html
#### 4.4 配置本地的yum，使之使用自建的yum源。
简单的来说，就是在本地或者客户机的/etc/yum.repos.d目录下新建一个配置文件文件（也可配置语句添加到已经存在文件中），以.repo为文件名后缀，比如yjx.repo，然后内容大概如下：

[yjx-yum]
name=yjx-yum
baseurl=http://192.168.33.12/yjx/
enabled=1
gpgcheck=0

#### 4.5 更新yum源
yum clean all 　清除yum源缓存  
yum repolist　　列出可用yum源


