def divisor(a):
    divisors= []
    for x in range(1,a+1):
        if a%x==0:
            divisors.append(x)
    print (divisors)

a=int (input("Enter a number"))
divisor(a)

