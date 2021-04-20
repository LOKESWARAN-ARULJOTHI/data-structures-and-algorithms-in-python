from random import shuffle
import time

def countingSort(array):
    start=time.time()
    size=len(array)
    output=[0]*size
    count=[0]*(max(array)+1)

    # update the count
    for element in array:
        count[element]+=1
    
    # cummulative add of count values 
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    
    # update back the output list 
    i=size-1
    while i>=0:
        output[count[array[i]]-1]=array[i]
        count[array[i]]-=1
        i-=1
    
    # copy it to given array
    for i in range(0,size):
        array[i]=output[i]
    stop=time.time()
    print('\nTime taken to sort:',stop-start,'secs')
    return array

if __name__=='__main__':

    arr=[]
    for i in range(1,1000001):
        arr.append(i)

    shuffle(arr)
    countingSort(arr)
    # print(arr)
    print('Counting sorting 1000000 numbers..\nFirst 5 numbers',arr[:5],'\nLast 5 numbers',arr[-5:])