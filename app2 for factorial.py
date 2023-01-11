#recurssive function
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) #5*4*3*2*1

num=5
print("factorial",num,"is",factorial(num))

'''we can put in single line with ternary operator
def factorial (n):
 return 1 if(n==0 or n==1) else n*factorial(n-1)
num=10
print("factorial",num,"is",factorial(num))'''