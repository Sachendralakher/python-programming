# number which can divided by 1 or self known as prime number ie. 19
num=int(input("enter number"))
count=0
for i in range(1,num+1):
    if (num%i)==0:
            count=count+1
if count == 2:
        print("number prime")
else:
        print("not prime")
if num==1:
    print("please enter greater than 1")
