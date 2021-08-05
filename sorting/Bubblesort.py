arr=[10,15,4,23,0]
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

#[0, 4, 10, 15, 23]

