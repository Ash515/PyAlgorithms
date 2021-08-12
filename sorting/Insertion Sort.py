def InsertionSort(list1):
    for index in range(1,len(list1)):
        curr=list1[index]
        pos=index
        while curr<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos-=1
        list1[pos]=curr

lis=[10,4,8,2,1]
InsertionSort(lis)
print(lis)  #[1, 2, 4, 8, 10]


