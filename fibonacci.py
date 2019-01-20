def fibonacci(num):
    a=1
    b=1
    l=[]
    for i in range(1,num+1):
        c=a+b
        l.append(a)
        a=b
        b=c

    print(l)

num=int(input ("Enter the last number of the series"))
fibonacci(num)



