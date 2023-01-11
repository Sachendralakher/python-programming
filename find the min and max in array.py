arr=[1,2,10,25]
max=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)


#for min
arr=[1,2,32,54]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)