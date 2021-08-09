def pivot_place(list1,first,last):
    pivot=list1[first]
    left=first
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        
        if left>right:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
    

def quicksort(list1,first,last):
    if first<last:
        p=pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)

#driver code
array=[20,30,10,50,70,100]
quicksort(array,0,len(array)-1)

print(array)  #[10, 20, 30, 50, 70, 100]














































