def binarySearch(array,element):
    first=0
    last=len(array)-1
    found=False

    while first<=last and not found:
        mid=(first+last)//2

        if array[mid]==element:
            found=True
        elif array[mid]<element:
            first=mid+1
        else:
            last=mid-1
    return found

if __name__=='__main__':
    array=[]
    items=input('Enter the ordered list:').split(',')
    for item in items:
        array.append(int(item))
    element=int(input('Enter the Element to be searched:'))
    print(binarySearch(array,element))