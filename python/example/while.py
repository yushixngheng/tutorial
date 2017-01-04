a=7

while a:

    print "hello%s" % a

    a=a-1





for i in [1,2,3,4,5]:

    print i



for i in range(1, 7):

    print "hello %s " % i



for i in range(1, 10, 5):

    print "hello %s " % i







for i in range(1, 10):

    if i%2 == 0 :

        print "%s 偶数" % i

    else:

        print "%s 奇数" % i







a=1

while a < 7:

    a = a+1

    if a == 3:

        continue

    print a

