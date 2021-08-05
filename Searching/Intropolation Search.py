def Interpolation(arr,x):
    l=0
    h=len(arr)-1
    while l<=h and x>=l and  x<=h:
        if (l==h):
            if(arr[l]==x):
                return l
            return -1
        pos=l+int(((float(h-l)/(arr[h]-arr[l])))*(x-arr[l]))
        if(x==arr[pos]):
            return pos
        elif(x>arr[pos]):
             l=arr[pos]+1
        elif(x<arr[pos]):
             h=arr[pos]-1
    return -1
array=[]
size=int(input("Enter the size of an array:"))
for i in range(size):
    values=int(input("Enter the values:"))
    array.append(values)
array.sort()
print("Your sorted array is,",array)
search=int(input("Enter the search value:"))
res=Interpolation(array,search)
print("Your value found at ",res)

