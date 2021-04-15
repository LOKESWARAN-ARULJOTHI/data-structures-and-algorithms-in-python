class Node(): #create a Node class
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

# Create a Hash Table class
class Hash():
    # Initialize the array for hash
    def __init__(self):
        self.capacity=7
        self.hash=[None]*self.capacity #array
        self.n=0
    
    # Create a hashing function  
    def hashing(self,key):
        hashvalue=0
        for char in key:
            hashvalue+=ord(char)
        return hashvalue% self.capacity #value % cap
    
    # Inserting an key value pair in hash 
    def __setitem__(self,key,value):
        index=self.hashing(key)
        if self.hash[index]==None:
            self.hash[index]=Node(key,value)
            self.n+=1
            return
        else:
            node=self.hash[index]
            prev=None
            while node:
                if node.key==key:
                    node.value=value
                    return
                prev=node
                node=node.next
            node=Node(key,value)
            prev.next=node
            self.n+=1
            if self.n > len(self.hash)//2:
                self.resize(2*len(self.hash)-1) # 2*length of arr

    # Returns the value for the given key 
    def __getitem__(self,key):
        index=self.hashing(key)
        if self.hash[index]==None:
            print('There is no item with this key\n')
            return
        node=self.hash[index]
        while node:
            if node.key==key:
                print(f'"{node.key}" : "{node.value}"\n')
                return
            node=node.next
        print('There is no item with this key\n')
    
    # Deletes the given key and their value 
    def __delitem__(self,key):
        index=self.hashing(key)
        if self.hash[index]==None:
            print('There is no item with this key\n')
            return
        node=self.hash[index]
        prev=None
        while node:
            if node.key==key:
                self.n-=1
                print(f'Key "{node.key}" with Value "{node.value}" is deleted\n')
                if prev:
                    prev.next=node.next
                else:
                    self.hash[index]=None
                # if self.n <= len(self.hash)//4:
                #     self.resize((len(self.hash)//2)+1)
                return
            prev=node
            node=node.next
        print('There is no item with this key\n')
    
    # Resizing function
    def resize(self,capacity):
        old=[]
        for element in self.hash:
            if element!=None:
                while element:
                    old.append(element)
                    element=element.next
        self.hash=[None]*capacity
        self.n = 0
        for item in old:
            self[item.key]=item.value
    
    # Prints the entire hash table
    def printHash(self):
        for item in self.hash:
            while item:
                print(f'Key "{item.key}" : "{item.value}"')
                item=item.next
        print(len(self.hash),'is the capacity of the Hash Table')
        return
                
# Main function
contact=Hash()
while True:
    operation=int(input('\n1.Add contact\n2.Delete contact\n3.Get contact\n4.Print Contacts\n5.Exit\n\nEnter your choice:'))
    if operation==1:
        key=input('\nEnter the name:')
        value=input('Enter the number:')
        contact[key]=value
    elif operation==2:
        key=input('\nEnter the name:')
        del contact[key]
    elif operation==3:
        key=input('\nEnter the name:')
        contact[key]
    elif operation==4:
        contact.printHash()
    elif operation==5:
        break
