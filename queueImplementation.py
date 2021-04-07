# Import collections.deque module
from collections import deque

# Create a class for Queue
class Queue():

    # Initialize the Queue
    def __init__(self):
        self.queue=deque()
    
    # Push function
    def enqueue(self,data):
        self.queue.append(data)
        print(data,'is added\n')

    # Pop function
    def deque(self):
        if self.isEmpty():
            print('Queue is empty\n')
            return
        value = self.queue.popleft()
        print(value,'is removed\n')
        
    # Prints the first element
    def peekFront(self):
        if self.isEmpty():
            print('Queue is empty\n')
            return        
        print(self.queue[0],'is the first element\n')
        
    # Prints the last element
    def peekRear(self):
        if self.isEmpty():
            print('Queue is empty\n')
            return
        print(self.queue[-1],'is the last element\n')


    # Checks if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
        
    # Returns the size of the queue
    def sizeOf(self):
        print(len(self.queue),'is the size\n')
    
    # Prints the Queue
    def printQueue(self):
        if self.isEmpty():
            print('Queue is empty\n')
            return
        for element in self.queue:
            print(element)
        print()
    
q=Queue()
while True:
    operation=int(input('1.Enqueue\n2.Deque\n3.PeekFront\n4.PeekRear\n5.Size of stack\n6.Print the queue\n7.Exit\n\nEnter your choice:'))
    if operation==1:
        data=input('Enter the data:')
        q.enqueue(data)
    elif operation==2:
        q.deque()
    elif operation==3:
        q.peekFront()
    elif operation==4:
        q.peekRear()
    elif operation==5:
        q.sizeOf()
    elif operation==6:
        q.printQueue()
    else:
        break