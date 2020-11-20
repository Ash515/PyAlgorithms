import math
def jump(arr,key):
    low=0
    inter=int(math.sqrt(len(arr)))
    for i in range(0,len(arr),inter) :
        if(arr[i]==key):
            return i
        elif(arr[i]<key):
            low=i
        else:
            break
    c=low
    for j in arr[low:]:
        if(key==j):
            return c
        c=c+1
arr=[]
size=int(input("Emter the size of array:"))
for k in range(size):
    values=int(input("Enter the array values:"))  
    arr.append(values)
arr.sort()
print("Your sorted array values:",arr)
search=int(input("Enter the search key:"))
result=jump(arr,search)
print("Your Result is,",result)

        
