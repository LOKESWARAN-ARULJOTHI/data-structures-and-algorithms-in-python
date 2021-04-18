def insertionSort(array):
    for i in range(1,len(array)):
        currentValue=array[i]
        position=i
        while position>0 and array[position-1]> currentValue:
            array[position]=array[position-1]
            position=position-1
        array[position]=currentValue

arr=[5,4,2,84,7,6,12,54,85,65,215,352,545,12]
insertionSort(arr)
print(arr)