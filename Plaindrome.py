def palaindrome(a):
# back=a[::-1]
# print(a)
# print(back)
    if a[0:]==a[::-1]:
        print ("String is a plaindrome")
    else:
        print ("not a plaindrome")

a=input ("Enter a string:")
palaindrome(a)
