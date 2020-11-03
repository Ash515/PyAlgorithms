def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1                                                                                                                                                                                                                                                                                                                                                                                                                                       

alist=str(input("Enter the list of values:"))
alist=alist.split()
alist=[int(x) for x in alist]
key=int(input("Enter the Key value:"))

index=linearsearch(alist,key)
if index<0:
    print("{} was no found".format(key))
else:
    print("{} was found at the position of{}".format(key,index))
