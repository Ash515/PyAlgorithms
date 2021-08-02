#Acending Order
list1=[56,3,2,78,6,0]
print("Unsorted list",list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_ind=list1.index(min_val,i)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)  #[0, 2, 3, 6, 56, 78]

#Descending Order

list1=[56,3,2,78,6,0]
print("Unsorted list",list1)
for i in range(len(list1)):
    min_val=max(list1[i:])
    min_ind=list1.index(min_val,i)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)  #[78, 56, 6, 3, 2, 0]