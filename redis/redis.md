# Redis study
## 1.简介
Redis是一个开源的、高性能的，基于键值对缓存与存储系统，通过提供多种键值数据类型来适应不同场景下的缓存与存储需求。同时Redis的诸多高层级功能使其可以胜任消息队列、任务队列等不同的角色。
## 2.特色
Redis数据库中的所有数据都是存储在内存中，由于内存的读写速度远快于硬盘，因此Redis在性能上的对比其他基于硬盘存储的数据库有非常明显的优势。  
将数据存储在内存中也有问题，比如程序退出后内存中的数据会丢失。不过Redis提供了对持久化的支持，即可以将内存中的数据异步写入到硬盘中，同时不影响继续提供服务。  
Redis虽然是作为数据库开发的，但由于其提供了丰富的功能，很多人将它作为缓存，队列系统等。    
Redis是一个速度非常快的非关系数据库(non-relational database),它可以存储键(key)与5种不同类型的值(value)之间的映射(mapping),可以将存储在内存的键值对数据持久化到硬盘，可以使用复制特性来扩展读性能还可以使用客户单分片来扩展写性能。  

Redis提供了十几种不同编程语言的客户端库，这些库都很好的封装了Redis的命令，使得在程序中与Redis进行交互变得更容易。  
注：在性能上Redis是单线程模型，而Memcached支持多线程，所以在多核服务器上Memcached的性能理论上相对更高一些。  Redis能够自动以两种不同的方式将数据写入硬盘，并且Redis除了能存储普通的字符串键之外，还可以存储4种数据结构，而memcached只能存储普通的字符串键。
Redis既可以用作主数据库(primary database)使用，又可以作为其他存储系统的辅助数据库(auxiliary database)使用。
## 3.redis安装
wget http://download.redis.io/redis-stable.tar.gz  
tar -zxvf redis-stable.tar.gz   
cd redis-stable  
make  
make install
### 3.1启动
redis-server
### 3.2 通过初始化脚本启动redis
### 3.3 Redis命令行客户端
redis-cli是Redis自带的基于命令行的Redis客户端。
### 3.4 多数据库
每个数据库对外都是以一个0开始递增数字命名的，Redis默认支持16个数去库，可以通过配置参数databases来修改这一数字。客户端与Redis建立连接后会自动选择0号数据库，不过可以随时使用SELECT命令来切换数据库。如要选择1号数据库：  
redis> SELECT 1  
OK  
redis [1]> GET foo  
(nil)  
注：Redis不支持自定义数据库的名字，每个数据库都已编号命名，开发者必须自己记录哪些数据库存储了哪些数据。另外Reids也不支持为每个数据库设置不同的访问密码，所以一个客户端要么可以访问全部数据库，要么连一个数据库也不能访问。最重要的一点是多个数据库之间并不是完全隔离的，比如FLUSHALL命令可以清空一个Redis实例中所有数据库中的数据。
## 4.数据类型
### 4.1 字符串类型
字符串类型是Redis中最基本的数据类型，它能存储任何形式的字符串，包括二进制数据。你可以用其储存用户的邮箱、JSON化的对象甚至是一张图片。一个字符串类型键允许存储的数据的最大容量是512MB.  
字符串类型是其他四种数据类型的基础，其他数据类型和字符串类型的差别从某种角度来说只是组织字符串的形式不同。例如，列表类型是以列表的形式组织字符串，而集合类型是以集合的形式组织字符串。
#### 4.1.1 命令
SET key value  
GET key  
INCR key  
INCRBY key increment  
DECR key decrement  
INCRBYFLOAT key increment  
APPEND key value  
MSET key value [key value ...]  
MGET key [key ...]  
GETBIT key offset  
SETBIT key offset value  
BITCOUNT key [start] [end]  
BITOP operation destkey key [key ...]  
### 4.2 散列类型
我们现在已经知道Redis是采用字典结构以键值对的形式存储数据的，而散列数据(hash)的键值也是一种字典结构，其存储了字段(field)和字段值的映射，但字段值只能是字符串，不支持其他数据类型，换句话说，散列类型不能嵌套其他的数据类型。一个散列类型键可以包含只多  
```math
2^{32}-1
```
个字段。  
注：除了散列类型，Redis的其他数据类型同样不支持数据类型的嵌套。比如集合类型的每个元素都只能是字符串，不能是另一个集合或散列表等。
#### 4.2.1 命令
HSET key field value  
HGET key field  
HMSET key field value [field value ...]  
HMGET key field [field ...]  
HGETALL key  
HEXISTS key field  
HDEL key field [field ...]  
HKEYS key  
HVALS key  
HLEN key  
### 4.3 列表类型
列表类型(list)可以存储一个有序的字符串列表，常见的操作是向列表两端添加元素，或者获取列表的某一个片段。  
列表类型内部是使用双向链表(double linked list)实现的，所以向列表两端添加元素的时间复杂度为O(1),获取越接近两端的元素速度就越快。但是使用链表的代价是通过索引的访问元素比较慢。与散列列表键最多容纳的字段数量相同，一个列表类型键最多容纳的字段数量相同，一个列表类型键最多容纳
```math
2^{32}-1
```
个元素
#### 4.3.1 命令
LPUSH key value [value ...]  
RPUSH key value [value ...]  
LPOP key  
RPOP key  
LLEN key  
LRANGE key start stop  
LREM key count value  
LINDEX key index  
LSET key index value  
LINSET key BEFORE|AFTER pivot value  
RPOPLPUSH source destination  
#### 4.4 集合类型
在集合中每个元素都是不同的，且没有顺序的。一个集合类型(set)键可以存储至多
```math
2^{32}-1
```
个字符串。  
集合类型的常用操作是向集合中加入或删除元素，判断某个元素是否存在等，由于集合类型在Redis内部是使用值为空的散列表(hash table)实现的，所以这些操作的时间复杂度都是O(1).最方便的是多个集合类型键之间还可以进行并集、交集和差集运算。
#### 4.4.1 命令
SADD key member [member ...]  
SREM key member [member ...]  
SMEMBERS key  
SISMEMBER key member  
SDIFF key [key ...]  
SINTER key [key ...]  
SUNION key [key ...]  
SCARD key  
SINTERSTORE destination key [key ...]  
SUNIONSTORE destination key [key ...]  
SRANDMEMBER key [count]  
SPOP key  
### 4.5 有序集合类型
在集合类型的基础上有序集合类型为集合中的每个元素都关联了一个分数，这使得我们不仅可以完成插入、删除和判断元素是否存在等集合类型支持的操作，还能够获取分数最高
（或最低）的前N个元素、或得指定分数范围内的元素等与分数有关的操作。虽然集合中的每个元素都是不同的，但是它们的分数却是可以相同。
#### 4.5.1 命令
ZADD key scoer member [score member ...]  
ZSCORE key member     
ZRANGE key start stop [WITHSCORES]  
ZREVRAGNGE key start stop [WITHSCORES]  
ZRANGEBYSCORE key min max [WITHSCOERS] [LIMIT offset count]  
ZINCRBY key increment member  
ZCARD key  
ZCOUNT scoreboard 90 100  
ZREM key member [member ...]  
ZREMRANGEBYRANK key star stop  
ZREMRANGEBYSCORE key min max  
ZRANK key member  
ZREVRANK key member  
## 5 实践
在此之前我们进行的操作都是通过Redis的命令行客户端redis-cli进行的，并没有介绍实际编程时如何操作Redis。本章将通过4个实例分别介绍Redis的PHP、Python、Ruby和Node.js客户端的使用方法。
### 5.1 PHP与Redis
Redis官方推荐的PHP客户端是Predis和phpredis。前者是完全使用PHP代码实现的原生客户端，而后者测试用C语言编写的PHP扩展。
#### 5.1.1 安装
#### 5.1.2 使用方法
#### 5.1.3 实践
### 5.2 Ruby与Redis
Redis官方推荐的Ruby客户端是redis-日报，也是各种语言的Redis客户端中最为稳定的一个。
#### 5.2.1 安装
#### 5.2.2 使用方法
#### 5.2.3 实践
### 5.3 Python与Redis
Redis官方推荐的Pyton客户端是redis-py
#### 5.3.1 安装
在linux下为Python语言安装Redis客户端库  
wget http://peak.telecommunity.com/dist/ez_setup.py  
python ez_setup.py  
python -m easy_install redis hiredis
#### 5.3.2 使用方法
#### 5.3.3 实践
### 5.4 Node.js与Redis
Redis官方推荐的Node.js的Redis客户端可以选择的有node_redis和ioredis。
#### 5.4.1 安装
#### 5.4.2 使用方法
#### 5.4.3 实践
## 6 脚本


