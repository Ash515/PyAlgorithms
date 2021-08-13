def shellsort(list1):
    gap=len(list1)//2
    while gap>0:
        for index in range(gap,len(list1)):
            curr=list1[index]
            pos=index
            while pos>=gap and curr<list1[pos-gap]:
                list1[pos]=list1[pos-gap]
                pos-=gap
            list1[pos]=curr
        gap=gap//2
    

arr=[10,23,15,20,56,67,12]
shellsort(arr)
print(arr)

#[10, 12, 15, 20, 23, 56, 67]