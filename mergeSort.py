def mergeSort(array):
    if len(array)>1:
        mid=len(array)//2

        leftHalf=array[:mid]
        rightHalf=array[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                array[k]=leftHalf[i]
                i+=1
            else:
                array[k]=rightHalf[j]
                j+=1
            k+=1
        
        while i < len(leftHalf):
            array[k]=leftHalf[i]
            i+=1
            k+=1

        while j < len(rightHalf):
            array[k]=rightHalf[j]
            j+=1
            k+=1
    print('Merging..',array)
    
if __name__=='__main__':
    arr=[9,8,7,4,5,6,3,2,1,-25]
    print('\nThe unsorted array is...\n',arr,end='\n\n')
    mergeSort(arr)
    print('\nThe sorted array is...\n',arr,end='\n\n')