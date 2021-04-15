def binarySearch(array,element):
    # base case 
    if len(array)==0: 
        return False
    
    else:
        mid=len(array)//2

        if array[mid]==element:
            found=True

        # right half
        elif array[mid]<element:
            return binarySearch(array[mid+1:],element)

        # left half
        else:
            return binarySearch(array[:mid],element)
    return found

if __name__=='__main__':
    array=[]
    items=input('Enter the ordered list:').split(',')
    for item in items:
        array.append(int(item))
    element=int(input('Enter the Element to be searched:'))
    print(binarySearch(array,element))