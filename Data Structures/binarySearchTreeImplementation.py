class Node(): # Create a Node class
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
    
# Create a Binary Search Tree class
class BinarySearchTree():

    # Initialize root = None
    def __init__(self):
        self.root=None
    
    # Insert item in the root node 
    def insert(self,data):
        if not self.root:
            self.root=Node(data)
            print(data,'is added')
        else:
            self.insertNode(data,self.root)

    # Insert the data as either child 
    def insertNode(self,data,root):
        if data<root.data:
            if root.leftChild:
                self.insertNode(data,root.leftChild)
            else:
                root.leftChild=Node(data)
                print(data,'is added')
        elif data>root.data:
            if root.rightChild:
                self.insertNode(data,root.rightChild)
            else:
                root.rightChild=Node(data)
                print(data,'is added')
        elif data==root.data:
            print('Item is already existing the tree\n')

    # Delete a node
    def delete(self,data):
        if self.root:
            self.__remove(data,self.root)
    
    def __remove(self,data,root):
        if not root:
            return None
        if data<root.data:
            root.leftChild=self.__remove(data,root.leftChild)
        elif data>root.data:
            root.rightChild=self.__remove(data,root.rightChild)
        elif data == root.data:
            if not root.leftChild and not root.rightChild:
                # print('Removing leaf node')
                del root
                return None
            elif not root.leftChild:
                tempNode=root.rightChild
                del root
                # print('Removing node with 1 child')
                return tempNode
            elif not root.rightChild:
                tempNode=root.leftChild
                del root
                # print('Removing node with 1 child')
                return tempNode
            else:
                # print('Removing node with 2 child')
                tempNode=self.__predecessor(root.leftChild)
                root.data=tempNode.data
                root.leftChild=self.__remove(tempNode.data,root.leftChild)
        return root

    # Traverse throught the tree 
    def printTree(self):
        if self.root:
            self.traverseInOrder(self.root)
        else:
            print('Tree is empty')
    
    # Inorder Traversal
    def traverseInOrder(self,root):
        if root.leftChild:
            self.traverseInOrder(root.leftChild)
        
        print('%s' %root.data)

        if root.rightChild:
            self.traverseInOrder(root.rightChild)
    
    # Search an item
    def search(self,data):
        if self.root:
            return self.__search(data,self.root)
    
    def __search(self,data,root):
        if data< root.data:
            if root.leftChild:
                return self.__search(data,root.leftChild)
        elif data> root.data:
            if root.rightChild:
                return self.__search(data,root.rightChild)
        elif data==root.data:
            return True
        return False
        
    # Get the minimum value 
    def getMinValue(self):
        if self.root:
            return self.__getMin(self.root)
    
    def __getMin(self, root):
        if root.leftChild:
            return self.__getMin(root.leftChild)
        return root.data

    # Get the maximum value 
    def getMaxValue(self):
        if self.root:
            return self.__getMax(self.root)

    def __getMax(self, root):
        if root.rightChild:
            return self.__getMax(root.rightChild)
        return root.data

    # Finds the predecessor node
    def __predecessor(self, root):
        if root.rightChild:
            return self.__predecessor(root.rightChild)
        return root


# Main function
bst=BinarySearchTree()
while True:
    operation=int(input('\n1.Add item\n2.Delete item\n3.Search item\n4.Print items\n5.Get Maximum\n6.Get Minimum\n7.Exit\n\nEnter your choice:'))
    if operation==1:
        value=input('Enter the item:')
        bst.insert(value)
    elif operation==2:
        value=input('Enter the item:')
        bst.delete(value)
    elif operation==3:
        value=input('Enter the item:')
        print(bst.search(value))
    elif operation==4:
        print("Tree:")
        bst.printTree()
    elif operation==5:
        print('%s is the maximum item' %bst.getMaxValue())
    elif operation==6:
        print('%s is the maximum item' %bst.getMinValue())
    else:
        break
