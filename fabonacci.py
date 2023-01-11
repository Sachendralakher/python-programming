#0,1,1,2,3,5,8,13 add of before 2 number
a=0
b=1
print(a)
print(b)
for i in range(1,15):
    sum=(a+b)
    a=b
    b=sum
    print(sum)