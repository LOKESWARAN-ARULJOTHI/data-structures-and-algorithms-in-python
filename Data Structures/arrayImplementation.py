class array():
    def __init__(self):
        self.array=[]
        
    def add(self,element): #Add element at the last --> O(1)
        return self.array.append(element)

    def insert(self,pos,element): #Add element at a position --> O(n)
        self.array.insert(pos,element)

    def delete(self,position=-1): #Delete element at the last or at a position -->O(N)
        print("Deleted element is :",self.array.pop(position),'\n')

    def remove(self,element): #Delete a particular element --> O(N)
        self.array.remove(element)
        print(element,'is removed\n')


    def printArray(self): #Traverse and print the array -->O(N)
        for element in self.array:
            print(element)
        print("")

    def search(self,element): #Search an element --> O(N)
        print(element,'is at',self.array.index(element),'th index\n')

arr = array()
inp=input('Enter the array:').split(',')
for i in inp:
    arr.add(int(i)) #adding
arr.printArray() #traverseing
arr.delete(1) #deleteing
arr.delete(2)
arr.insert(4,55) #inserting
arr.add(10)
arr.remove(8)
arr.search(1) #searching
arr.printArray()
