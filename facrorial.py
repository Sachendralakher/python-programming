#5*4*3*2*1=120 with the help of loop
factorial=1
num=0
if num<0:
    print("does not exist for negative umber")
elif num==0:
    print("this is factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of ",num,"is",factorial)
