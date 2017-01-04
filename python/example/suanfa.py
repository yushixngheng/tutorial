#快排的实现

def kp(arr, i, j):  #快排总调用函数

    if i<j:

        base = kpgc(arr, i, j)

        kp(arr, i, base)

        kp(arr, base+1, j)



def kpgc(arr, i, j):    #快排排序过程

    base = arr[i]

    while i<j:

        while i<j and arr[j]>=base:

            j-=1

        while i<j and arr[j]<base:

            arr[i]=arr[j]

            i+=1

            arr[j]=arr[i]

    arr[i]=base

    return i



        

#选择排序的实现

def xzpx(arr):  #选择排序

    for i in range(0, len(arr)):    #每一趟排序

        k=i

        for j in range(i+1, len(arr)):  #每一趟选择最小的这个数

            if arr[j]<arr[k]:

                k=j

        arr[i],arr[k]=arr[k],arr[i] #交换位置





#二路归并排序

def gb(arr):    #第一次归并排序，以及持续调用rg()函数进行后续的归并排序

    arr_t=[[arr[0]]]#把传进去的数组的元素变为数组的形式，因为后续需要使用到

    k=0

    m=""

    if len(arr)%2==0:   #如果原数组长度为偶数，那么l的值为均数

        l=len(arr)/2

    else:               #如果原数组长度为奇数，那么l的值为一半后再加一位

        l=len(arr)/2+1

    for t in range(0,l):

        m="h"+m

        arr_rg=list(m)  #生成一个存储数据的列表arrt_rg,此列表长度为l

    for i in range(1,len(arr)):

        arr_t = arr_t+[[arr[i]]]    #生成一个列表，该列表将原列表的元素变为列表，即两层列表

                                    #因为我们要调用后面的rg函数，该函数数据类型为列表

    if len(arr_t)%2==0:             #进行第一次归并排序，首先进行元素个数为偶数的情况

        for i in range(0, len(arr_t), 2):   #从第0位元素开始，每次增加2

            arr_rg[k]=dg(arr_t[i],arr_t[i+1])#第i位和i+1位进行排列

            k+=1

    else:                           #若元素个数为奇数

        for i in range(0,len(arr_t)-2,2):   #循环部分先进行偶数位数部分的排序，跟%2==0情况一样

            arr_rg[k]=dg(arr_t[i],arr_t[i+1])

            k+=1

        arr_rg[k]=arr_t[len(arr_t)-1]   #偶数部分排完后，单出一位奇数位，直接将奇数位

                                        #移到新存储数组arr_rg最后一位即可

    n = 0

    while 1:#第一趟归并完成后，还需要进行后续的归并，那么后续的归并一直调用arr_rg函数，直到长度为1为止

        if len(arr_rg)==1:#长度为1的时候，不需要归并，此时停止

            break

        else:

            arr_rg=rg(arr_rg)#否则调用arr_rg函数。调用的参数第一次是上述第一次归并的结果

                             #第二次以及以后的参数是第一次的上一次的arr_rg函数的执行结果

    return arr_rg 



def rg(arr_rg):     #依次对arr_rg进行二路归并

    k=0

    s=len(arr_rg[0])#s代表每组多少个元素，len(arr_rg)代表一共有多少组，l代表要比较多少次

    l=len(arr_rg)   #代表一共有多少组

    if len(arr_rg)%2==0:    #如果组的个数为偶数

        for i in range(0, len(arr_rg), 2):

            #将两个有序列表arr_rg[i], arr_rg[i+1]用dg函数合并为一个有序列表

            arr_rg[k]=dg(arr_rg[i], arr_rg[i+1])

            k+=1

        arr_rg=arr_rg[:l/2]#因为arr_rg由二和一，会产生多余元素，将多余元素舍去

        return arr_rg

    else:    #如果组的个数为奇数

        for i in range(0, len(arr_rg)-2, 2):

            #将两个有序列表arr_rg[i], arr_rg[i+1]用dg函数合并为一个有序列表

            arr_rg[k]=dg(arr_rg[i], arr_rg[i+1])

            k+=1

        arr_rg=arr_rg[:l/2]+[arr_rg[len(arr_rg)-1]]#因为arr_rg由二和一，会产生多余元素，将多余元素舍去

        return arr_rg



def dg(arr1, arr2): #两个有序数列之间排序

    x=len(arr1) #x为有序列表arr1的长度

    y=len(arr2) #x为有序列表arr2的长度

    i=0

    j=0

    k=0

    m=""

    for t in range(0,x+y):

        m="h"+m

        









#归并排序

def mergeSort(arr):

    def merge(arr, temp, i, m, n):

        k = i

        j = m + 1

        while(i <= m and j <= n):

            if(arr[i] <= arr[j]):

                temp[k] = arr[i]

                i += 1

            else:

                temp[k] = arr[j]

                j += 1

            k += 1

        while(i <= m):

            temp[k] = arr[i]

            k += 1

            i += 1

        while(j <= n):

            temp[k] = arr[j]

            k += 1

            j += 1

    

    def mergePass(arr, temp, length):

        i = 0

        while(i+2*length < len(arr)):

            merge(arr, temp, i, i+length-1, i+2*length-1)

            i += 2 * length

        if(i+length < len(arr)):

            merge(arr, temp, i, i+length-1, len(arr)-1)

        else:

            j = i

            while(j < len(arr)):

                temp[j] = arr[j]

                j += 1

    

    temp = [0 for x in range(len(arr))]

    leng = 1

    while(leng < len(arr)):

        mergePass(arr, temp, leng)

        leng *= 2

        mergePass(temp, arr, leng)

        leng *= 2





#二分查找搜索算法

def efss(arr, x):

    i=0

    j=len(arr)-1

    for k in range(j/2+1):

        if i>j:

            print -1

        zj=(i+j)/2      #中间位置为i+j的和除以2

        if arr[zj] == x:

            return zj

        elif arr[zj]>x:

            j=zj-1

        else:

            i=zj+1



















        

        

