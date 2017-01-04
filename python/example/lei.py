#类和对象的实现

#类的实现，建立一个类的格式是： class 类名

class man:

    pass                #pass属于空语句，无意义，目的是为了保证程序的完整性，叫做占位语句

print man

w=man()

print w





#对象的实现，建立了类之后，再建立一个类的对象（也叫作类的实例），建立对象的方式可以直接在类后面

#加小括号即可





#以上我们实现了一个类下创建了一个对象。在一个类下可以创建多个实例





#方法及属性的实现



class women:

    pass

wangdama=women()



#如何查看一个实例的具有哪些属性

print wangdama.__dict__



#如何我一个实例添加属性

wangdama.toufa="huangse"

print wangdama.__dict__



#为其中一个实例添加了某属性之后，该类的其他实例的属性是否会受影响

lidama=women()

print lidama.__dict__



#如何查看一个实例所属类的属性

print wangdama.__class__.__dict__



#如何给某个实例所属类添加属性

wangdama.__class__.xiezi="heise"

print wangdama.__class__.__dict__

print women.__dict__

print wangdama.__dict__

print lidama.__dict__

print lidama.__class__.__dict__



#所以我们得出结论：在单独修改某个实例属性时，其他实例属性不受影响

#               若修改类属性，那么在该类下所有实例类的属性均受影响





#上面我们讲了属性如何创建，下面我们来说方法如何创建

class god:

    def a(self):        #这里的self是必须的，所有的方法，第一个参数必须是self

        print "好汉歌"   #代表所有实例共享他，不具备其他任何含义



zongguan=god()

zongguan.a()





#类常见的一些专有方法

#1.__init__,构造函数

class people:

    def hi(self):

        print 8899



    def __init__(self):

        a="A:how are you?"

        b="----B:Fine, thank you"

        print a+b



#2.__del__,析构函数

class friend:

    def hi(self):

        print 8899

    def __init__(self):

        print "我是init 最先调用"



    def __del__(self):

        a = "我是析构函数"

        b = "---对象生命周期结束啦，现在我得删除对象善后啦！"

        print a+b

#

#xiaohang=friend()

#xiaohang.hi()

#friend()

friend().hi()

    





















