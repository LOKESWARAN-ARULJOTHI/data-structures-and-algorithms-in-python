# Linear search for unordered list
def unordered_search(array,element):
    index=0
    found=False
    while index<len(array) and not found:
        if array[index] == element:
            found = True
        else:
            index+=1
    return found

# Linear search for ordered list
def ordered_search(array,element):
    index=0
    found=False
    stopped=False
    while index<len(array) and not found and not stopped:
        if array[index]==element:
            found=True
        elif array[index]>element:
            stopped=True
        else:
            index+=1
    return found

if __name__=="__main__":
    arr1=[]
    operation=int(input('The array is\n1.unordered\n2.ordered:'))
    if operation==1:
        items=input('Enter the unordered list:').split(',')
        for item in items:
            arr1.append(int(item))
        element=int(input('Enter the Element to be searched:'))
        print(unordered_search(arr1,element))
    if operation==2:
        items=input('Enter the ordered list:').split(',')
        for item in items:
            arr1.append(int(item))
        element=int(input('Enter the Element to be searched:'))
        print(ordered_search(arr1,element))