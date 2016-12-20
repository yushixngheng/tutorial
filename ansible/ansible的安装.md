# ansible的安装
## Ansible安装 

### 介绍  

Ansible是一种批量部署工具，现在运维人员用的最多的三种开源集中化管理工具有：  puppet,saltstack,ansible，各有各的优缺点，其中saltstack和ansible都是用python开发的。ansible其实准确的说只提供了一个框架，它要基于很多其他的python模块才能工作的，所以在安装ansible的时候你要再装很多其他的依赖包的。

　　好处之一是使用者可以开发自己的模块，放在里面使用。第二个好处是无需在客户端安装agent，更新时，只需在操作机上进行一次更新即可。第三个好处是批量任务执行可以写成脚本，而且不用分发到远程就可以执行。  
### 正文
注意：强烈建议升级python版本到2.6以上，不然运行会出错或者有些功能会没有，在编译安装其他包的时候也会因为兼容问题报错。

(1)、python2.7安装  
https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz  
tar xvzf Python-2.7.8.tgz  
cd Python-2.7.8  
./configure --prefix=/usr/local  
make   
make install  
将python头文件拷贝到标准目录，以避免编译ansible时，找不到所需的头文件
cd /usr/local/include/python2.7  
cp -a ./* /usr/local/include/  
备份旧版本的python，并符号链接新版本的python  
cd /usr/bin  
mv python python.old  
cd /usr/local/bin/  
rm python  
ln -s /usr/local/bin/python2.7  
/usr/local/bin/python  
rm -f /usr/bin/python  
cp /usr/local/bin/python2.7 /usr/bin/python

修改yum脚本，使其指向旧版本的python，已避免其无法运行  
vi /usr/bin/yum  
!/usr/bin/python  -->  #!/usr/bin/python2.6  
(2)、setuptools模块安装  
https://pypi.python.org/packages/source/s/setuptools/setuptools-7.0.tar.gz  
tar xvzf setuptools-7.0.tar.gz  
cd setuptools-7.0  
python setup.py install  

当出现错误时候  
RuntimeError: Compression requires the (missing) zlib module  
我们需要安装zlib和zlib-devel  
yum install zlib  
yum install zlib-devel  
安装完成后，重新编译   python2.7【不需要删除，只需要重新编译，make， make install 安装就行了】  
然后重新安装setuptools：  

(3)、pycrypto模块安装  
https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz  
tar xvzf pycrypto-2.6.1.tar.gz  
cd pycrypto-2.6.1  
python setup.py install  

(4)、PyYAML模块安装  
http://pyyaml.org/download/libyaml/yaml-0.1.5.tar.gz
tar xvzf yaml-0.1.5.tar.gz  
cd yaml-0.1.5  
./configure --prefix=/usr/local
make --jobs=`grep processor /proc/cpuinfo | wc -l`  
make install  

https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz  
tar xvzf PyYAML-3.11.tar.gz  
cd PyYAML-3.11  
python setup.py install  

(5)、Jinja2模块安装  
https://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-0.9.3.tar.gz    
tar xvzf MarkupSafe-0.9.3.tar.gz  
cd MarkupSafe-0.9.3  
python setup.py install  

https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.7.3.tar.gz  
tar xvzf Jinja2-2.7.3.tar.gz  
cd Jinja2-2.7.3  
python setup.py install  

(6)、paramiko模块安装  
https://pypi.python.org/packages/source/e/ecdsa/ecdsa-0.11.tar.gz  
tar xvzf ecdsa-0.11.tar.gz  
cd ecdsa-0.11  
python setup.py install  

https://pypi.python.org/packages/source/p/paramiko/paramiko-1.15.1.tar.gz  
tar xvzf paramiko-1.15.1.tar.gz  
cd paramiko-1.15.1  
python setup.py install  

(7)、simplejson模块安装  
https://pypi.python.org/packages/source/s/simplejson/simplejson-3.6.5.tar.gz  
tar xvzf simplejson-3.6.5.tar.gz  
cd simplejson-3.6.5  
python setup.py install  

(8)、ansible安装  
https://github.com/ansible/ansible/archive/v1.7.2.tar.gz    
tar xvzf ansible-1.7.2.tar.gz  
cd ansible-1.7.2  
python setup.py install  

(9)、SSH免密钥登录设置  
生成公钥/私钥
ssh-keygen -t rsa 
写入信任文件（将/root/.ssh/id_rsa.pub分发到其他服务器，并在所有服务器上执行如下指令）：  
cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys

(10)、拷贝，生成ansible配置文件
a 配置文件/etc/ansible/ansible.cfg  
mkdir -p /etc/ansible  
cp ansible-1.7.2/examples/ansible.cfg   /etc/ansible/  
b 配置文件/etc/ansible/hosts  
vim /etc/ansible/hosts  
[test]  
192.168.33.11  
192.168.33.12  

测试
ansible test -m command -a 'uptime'  
用来测试远程主机的运行状态  
ansible test -m ping  


查看看所有的参数  
ansible-doc -l

在做性能优化之前首先需要做的是收集一些统计数据，这样才能为后面做的性能优化提供数据支持，对比优化前后的结果。非常不错的是，在 github 发现一个 Ansible 任务计时插件“ansible-profile”，安装这个插件后会显示 ansible-playbook 执行每一个任务所花费的时间。  
Github 地址：https://github.com/jlafon/ansible-profile。  
这个插件安装很简单，只需要简单的三个命令即可完成安装。  
在你的 playbook 文件的目录下创建一个目录，目录名 callback_plugins 然后将下载的 profile_tasks.py 文件放到该目录下。  

cd /etc/ansible   
mkdir callback_plugins   
cd callback_plugins   
wget https://raw.githubusercontent.com/jlafon/ansible-profile/master/callback_plugins/profile_tasks.py  
