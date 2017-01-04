#树



#树的基本构造

Tree=[2, 3, [58, 6, [5]]]

print Tree[0]

print Tree[1]

print Tree[2]

Tree2 = Tree[2]

print Tree2[0]



#二叉树

'''

比如要构造一个二叉树

      7

  8      9

   23     36

 57  58

可以这样分析：

base = (-->8也就是jd2,-->9也就是jd3,base)

jd2=(no,-->23也就是jd4,8)

jd3=(no,-->36也就是jd5,9)

jd4=(-->57也就是jd6,-->58也就是jd7,23)

jd5=(no,no,36)

jd5=(no,no,57)

jd5=(no,no,58)

但是要注意，写的时候倒过来写

'''



class TRee():

    def __init__(self, leftjd=0, rightjd=0, data=0):

        self.leftjd = leftjd;

        self.rightjd = rightjd;

        self.data = data;



class Btree():

    def __init__(self, base=0):

        self.base = base

    def empty(self):

        if self.base is 0:

            return True

        else:

            return False

    def qout(self, jd):

        """前序遍历，NLR，根左右"""

        if jd==0 :

            return

        print jd.data

        self.qout(jd.leftjd)

        self.qout(jd.rightjd)

    def mout(self, jd):

        """前序遍历，NLR，根左右"""

        if jd==0:

            return

        self.mout(jd.leftjd)

        print jd.data

        self.mout(jd.rightjd)

    def hout(self, jd):

        """后序遍历，LRN，左右根"""

        if jd==0:

            return

        self.hout(jd.leftjd)

        self.hout(jd.rightjd)

        print jd.data

        





#链表的实现（单向链表）

class jd():

    def __init__(self, data):

        self.data = data

        self.next = None



class Linklist():

    def __init__(self, jd2):

        self.head = jd2

        self.head.next = None

        self.tail = self.head



    def add(self, jd2):

        self.tail.next = jd2

        self.tail = self.tail.next

        

    def view(self):

        jd2 = self.head

        linkstr = ""

        while jd2 is not None:

            if jd2.next is not None:

                linkstr=linkstr+str(jd2.data)+"-->"

            else:

                linkstr += str(jd2.data)

            jd2 = jd2.next

        print linkstr





#bitmap的实现

class Bitmap():

    def __init__(self, max):

        self.size = int((max+31-1)/31)

        self.array = [0 for i in range(self.size)]



    def bitIndex(self,num):

        return num%31



    def set(self,num):

        elemIndex = num/31

        byteIndex = self.bitIndex(num)

        elem = self.array[elemIndex]

        self.array[elemIndex] = elem |(1<<byteIndex)



    def test(self, i):

        elemIndex = i/31

        byteIndex = self.bitIndex(i)

        if self.array[elemIndex] &(1<<byteIndex):

            return True

        return False



if __name__ == '__main__':

    MAX = ord('z')

    suffle_array = [x for x in 'coledraw']

    result = []

    bitmap = Bitmap(MAX)

    for c in suffle_array:

        bitmap.set(ord(c))

    for i in range(MAX+1):

        if bitmap.test(i):

            result.append(chr(i))

    print "原始数组为: %s" % suffle_array

    print "排序后的数组为: %s" % result

    



#图的实现

chart={"A":["B","D"], "C":["E"], "D":["C","E"]}

def path(chart, x, y, pathd=[]):

    pathd = pathd+[x]

    if x==y:

        return pathd

    if not chart.has_key(x):

        return None

    for jd in chart[x]:

        if jd not in pathd:

            newjd=path(chart,jd,y,pathd)

            if newjd:

                return newjd





#栈的实现

class Stack():

    def __init__(st,size):

        st.stack=[]

        st.size=size

        st.top=-1



    def push(st,content):

        if st.Full():

            print "Stack is Full!"

        else:

            st.stack.append(content)

            st.top=st.top+1



    def out(st):

        if st.Empty():

            print "Stack is Empty"

        else:

            st.top= st.top-1 

        

    def Full(st):

        if st.top==st.size:

            return True

        else:

            return False



    def Empty(st):

        if st.top==-1:

            return True

        else:

            return False





#队列的实现

class Queue():

    def __init__(qu,size):

        qu.queue = []

        qu.size = size

        qu.head = -1

        qu.tail = -1



    def Empty(qu):

        if qu.head==qu.tail:

            return True

        else:

            return False



    def enQueue(qu, content):

        if qu.Full():

            print "Queue is Full!"

        else:

            qu.queue.append(content)

            qu.tail = qu.tail + 1



    def outQueue(qu):

        if qu.Empty():

            print "Queue is Empty!"

        else:

            qu.head = qu.head - 1

    

    def Full(qu):

        if (qu.tail-qu.head+1)== qu.size:

            return True

        else:

            return False







    

