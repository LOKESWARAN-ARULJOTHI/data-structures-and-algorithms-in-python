class Node(): #initialize Node class
    def __init__(self,data):
        self.data=data
        self.next=None

# Implement using Linked list 
class StackLL():
    # Initialize top 
    def __init__(self):
        self.top=None
        self.length=0
    
    # Push function
    def push(self,data):
        newNode=Node(data)
        if not self.top:
            self.top=newNode
            print(newNode.data,'is pushed\n')
            self.length+=1
        else:
            newNode.next=self.top
            self.top=newNode
            print(newNode.data,'is pushed\n')
            self.length+=1
    
    # Pop function
    def pop(self):
        if self.isEmpty():
            print('Stack is empty\n')
            return
        temp=self.top
        self.top=self.top.next
        temp.next=None
        print(temp.data,'is popped\n')
        self.length-=1

    # Peek function
    def peek(self):
        print(self.top.data,'is peeked\n')
        return self.top.data

    # Check if stack is empty
    def isEmpty(self):
        if self.length==0 and self.top==None:
            return True
        else:
            return False
    
    # Gives the size of the stack 
    def sizeOf(self):
        print(self.length,'is the length\n')
        return self.length
    
    # Print the stack
    def printStack(self):
        if self.isEmpty():
            print('Stack is empty\n')
            return
        node=self.top
        while node:
            print(node.data,'\n|')
            node=node.next
        print('None\n')

# Main Function
stack1=StackLL()
while True:
    operation=int(input('1.Push\n2.Pop\n3.Peek\n4.Size of stack\n5.Print the stack\n6.Exit\n\nEnter your choice:'))
    if operation==1:
        data=input('Enter the data:')
        stack1.push(data)
    elif operation==2:
        stack1.pop()
    elif operation==3:
        stack1.peek()
    elif operation==4:
        stack1.sizeOf()
    elif operation==5:
        stack1.printStack()
    elif operation==6:
        break
