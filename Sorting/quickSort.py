# Quick Sort
def quicksort(array,low,high):
    if low>=high:
        return
    
    pivot=partition(array,low,high)
    quicksort(array,low,pivot-1)
    quicksort(array,pivot+1,high)

# Partition function 
def partition(array,low,high):
    pivot=(low+high)//2
    swap(array,pivot,high) # swap the pivot value from mid to last

    i=low
    for j in range(low,high):
        if array[j]<array[high]: # Put the item in front if it is lower than the pivot value
            swap(array,i,j)
            i+=1
    swap(array,i,high) # Swap the pivot value to the sorted index
    return i
# Just a swapping function 
def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

if __name__=='__main__':
    arr=[21,45,-10,25,65,15,2,99,91]
    print('The unsorted array')
    print(arr,'\n')
    quicksort(arr,0,len(arr)-1)
    print('The sorted array')
    print(arr,'\n')