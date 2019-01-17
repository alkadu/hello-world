num=int (input("Enter a number to check"))
check= int (input("Enter a number to divide by"))
if num%4==0:
    print("Number is a multiple of 4")
elif num%2==0:
    print("Number is even")
else:
    print ("Number is odd")

if num%check==0:
    print ("number is divided evenly")
else:
    print ("number is not divided evenly")

