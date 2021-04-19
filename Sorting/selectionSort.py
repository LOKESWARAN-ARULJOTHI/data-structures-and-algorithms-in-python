def selectionSort(arr):
    for i in range(0,len(arr)-1):
        lowIndex=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[lowIndex]:
                lowIndex=j
        
        if lowIndex!=i:
            temp = arr[i]
            arr[i]=arr[lowIndex]
            arr[lowIndex]=temp
        print('\nSelection sorting...',arr)
    return arr

arr=[6,5,4,3,2,1]
selectionSort(arr)