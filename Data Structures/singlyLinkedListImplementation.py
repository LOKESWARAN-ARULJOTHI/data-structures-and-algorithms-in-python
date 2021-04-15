class Node(): #Node class
    def __init__(self,data):
        self.data=data
        self.next=None

# class for Linked List
class LinkedList():
    # initialize head=None
    def __init__(self):
        self.head=None

    # Inserting node at the head
    def insertHead(self,data):
        newNode=Node(data)
        temp=self.head
        self.head=newNode
        newNode.next=temp
        print(newNode.data, 'is added to the list')

    # Inserting newNode at a given position
    def insertAt(self,position,data):
        newNode=Node(data)
        if position<0 or position > self.length():
            print('Invalid position')
            return
        if position==0:
            self.insertHead(data)
            return
        else:
            prevNode=currNode=self.head
            currPos=0
            while True:
                if currPos == position:
                    prevNode.next=newNode
                    newNode.next=currNode
                    print(newNode.data, 'is added to the list')
                    break
                prevNode=currNode
                currNode=currNode.next
                currPos+=1

    # Inserting newNode at the end 
    def insertEnd(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        lastNode=self.head
        while True:
            if lastNode.next==None:
                lastNode.next=newNode
                print(newNode.data, 'is added to the list')
                break
            lastNode=lastNode.next
    
    # Deleting the head node 
    def deleteHead(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None
        print(temp.data, 'is deleted from the list')
        
    # Deleting the node at a particular position
    def deleteAt(self,position):
        if position<0 or position>self.length():
            print('Invalid position')
            return
        if position==0:
            self.deleteHead()
            return
        else:
            currNode=prevNode=self.head
            currPos=0
            while True:
                if currPos == position:
                    prevNode.next=currNode.next
                    print(currNode.data, 'is deleted from the list')
                    currNode.next=None
                    break
                prevNode=currNode
                currNode=currNode.next
                currPos+=1
    
    # Deleting the last node 
    def deleteEnd(self):
        if self.isEmpty():
            print('The list is empty')
            return
        lastNode=self.head
        while lastNode.next!=None:
            prevNode=lastNode
            lastNode=lastNode.next
        prevNode.next=None
        print(prevNode.data, 'is deleted from the list')
    
    # print the Linked list 
    def printList(self):
        print()
        if self.isEmpty():
            print('The list is empty')
            return
        lastNode=self.head
        while lastNode:
            print(lastNode.data,'->',end=' ')
            lastNode=lastNode.next
        print('None\n')

    # Check if list is empty
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Returns the length of the List 
    def length(self):
        currNode=self.head
        length=0
        while currNode:
            length+=1
            currNode=currNode.next
        return length
        
#Main func
days=LinkedList() #Head -> None
days.printList()

days.insertHead('Tuesday') #Tuesday -> None
days.insertEnd('Wednesday') #Tuesday -> Wednesday -> None
days.insertEnd('Friday') #Tuesday -> Wednesday -> Friday -> None
days.printList()

days.deleteEnd() #Tuesday -> Wednesday -> None
days.insertAt(0,'Monday') #Monday -> Tuesday -> Wednesday -> None
days.printList()

days.deleteAt(0)
days.insertHead('Monday')
days.insertEnd('Thursday')
days.insertEnd('Friday')
days.insertEnd('Saturday')
days.insertEnd('Sunday')
days.printList()
