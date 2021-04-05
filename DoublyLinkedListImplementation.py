class Node(): #Node Class
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

# Doubly Linked list class 
class Doubly():
    # Initialize head and tail node 
    def __init__(self):
        self.head=self.tail=None
    
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
    
    # Inserting at the Head
    def insertHead(self,data):
        newNode=Node(data)
        if self.head==None and self.tail==None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        print(newNode.data,'is added')
    
    # Inserting at a particular position
    def insertAt(self,position, data):
        print(position)
        if position<1 or position>self.length()+1:
            print('Invalid position')
            return
        newNode=Node(data)
        if position==1:
            self.insertHead(data)
            return
        else:
            currPos=1
            currNode=self.head
            while True:
                if currPos==position:
                    newNode.prev=currNode.prev
                    currNode.prev.next=newNode
                    currNode.prev=newNode
                    newNode.next=currNode
                    print(newNode.data,'is added')
                    break
                currNode=currNode.next
                currPos+=1
    
    def insertEnd(self,data):
        if self.head==None and self.tail==None:
            self.insertHead(data)
            return
        newNode=Node(data)
        self.tail.next=newNode
        newNode.prev=self.tail
        self.tail=newNode
        newNode.next=None
        print(newNode.data,'is added')
    
    # Deleting the head node 
    def deleteHead(self):
        if self.isEmpty():
            print('The playlist is empty')
            return
        temp=self.head
        if self.head.next:
            self.head=self.head.next
        temp.next=None
        print(temp.data, 'is deleted')
    
    # Deleting the node at a particular position
    def deleteAt(self,position):
        if position<1 or position>=self.length()+1:
            print('Invalid position')
            return
        if position==1:
            self.deleteHead()
            return
        else:
            currNode=self.head
            currPos=1
            while True:
                if currPos == position:
                    currNode.prev.next=currNode.next
                    currNode.next.prev=currNode.prev
                    print(currNode.data, 'is deleted')
                    currNode.next=currNode.prev=None
                    break
                currNode=currNode.next
                currPos+=1

    # Deleting the last node 
    def deleteEnd(self):
        if self.isEmpty():
            print('The playlist is empty')
            return
        temp=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        temp.prev=None        
        print(temp.data, 'is deleted')

    # print the Linked list 
    def printList(self):
        print()
        if self.isEmpty():
            print('The playlist is empty')
            return
        lastNode=self.head
        print('Music Playlist\nHead <=>',end=' ')
        while lastNode:
            print(lastNode.data,'<=>',end=' ')
            lastNode=lastNode.next
        print('Tail\n')
    
#Main function
playlist=Doubly()

playlist.printList()
while True:
    operation=int(input('1.Add at top\n2.Add at last\n3.Update the playlist\n4.Delete at top\n5.Delete at last\n6.Delete at middle\n0.Exit\n\nChoose one operation:'))
    if operation==1:
        song=input('\nEnter the song:')
        playlist.insertHead(song)
        playlist.printList()
    elif operation==2:
        song=input('\nEnter the song:')
        playlist.insertEnd(song)
        playlist.printList()
    elif operation==3:
        position=int(input('\nEnter the position:'))
        song=input('Enter the song:')
        playlist.insertAt(position,song)
        playlist.printList()
    elif operation==4:
        playlist.deleteHead()
        playlist.printList()
    elif operation==5:
        playlist.deleteEnd()
        playlist.printList()
    elif operation==6:
        position=int(input('\nEnter the position:'))
        playlist.deleteAt(position)
        playlist.printList()
    else:
        break