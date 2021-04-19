def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        print()
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                print('Bubble sorting:',arr)
    return arr

array=[6,5,4,3,2,1]
print(bubbleSort(array))