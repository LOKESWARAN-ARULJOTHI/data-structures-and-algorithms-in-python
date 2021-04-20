from random import shuffle
import time

def countingSort(array,place):
    size=len(array)
    output = [0]*size
    count = [0]*10
    
    for i in range(0,size):
        index = array[i]//place
        count[index%10]+=1
    
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    
    i=size-1
    while i>=0:
        index = array[i]//place
        output[count[index%10]-1]=array[i]
        count[index%10]-=1
        i-=1

    for i in range(0,size):
        array[i]=output[i]
    return arr

def radixSort(array):
    start=time.time()
    maximum=max(array)
    place=1
    while maximum//place > 0:
        countingSort(array,place)
        place *= 10
    stop=time.time()
    print('\nTime taken to sort:',stop-start,'secs')
    return array

if __name__=='__main__':
    arr=[]
    for i in range(1,1000001):
        arr.append(i)

    shuffle(arr)
    radixSort(arr)
    # print(arr)
    print('Radix Sorting 1000000 numbers..\nFirst 5 numbers',arr[:5],'\nLast 5 numbers',arr[-5:])