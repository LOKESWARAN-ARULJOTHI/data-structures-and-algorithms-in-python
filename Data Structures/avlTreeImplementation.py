# Create a Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild= None
        self.height=0

# Create a AVL TREE class
class avlTree():

    # Initialize root = None
    def __init__(self):
        self.root=None
    
    # Gives the height of the Node
    def calcHeight(self,node):
        if not node:
            return -1
        
        return node.height
    
    #Gives the diff between left and right sub tree
    def checkBalanced(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def insert(self,data):
        self.root=self.insertNode(data,self.root)
    
    def insertNode(self,data ,node):
        if not node:
            return Node(data)
        
        if data<node.data:
            node.leftChild=self.insertNode(data,node.leftChild)
        elif data>node.data:
            node.rightChild=self.insertNode(data,node.rightChild)
        elif data==node.data:
            print('Item already exists')
        node.height=max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) +1
        return self.settleViolation(data,node)

    def settleViolation(self,data,node):
        balanced=self.checkBalanced(node)

        #double left heavy
        if balanced>1 and data<node.leftChild.data:
            print('Right right rotation')
            return self.rightRotate(node)
            
        #double right heavy
        if balanced<-1 and data>node.rightChild.data:
            print('Left left rotation')
            return self.leftRotate(node)
        
        # left right heavy
        if balanced>1 and data>node.leftChild.data:
            print('Left right rotation')
            node.leftChild=self.leftRotate(node.leftChild)
            return self.rightRotate(node)

        # right left heavy
        if balanced<-1 and data<node.rightChild.data:
            print('Right left rotation')
            node.rightChild=self.rightRotate(node.rightChild)
            return self.leftRotate(node)
        return node

        # Delete a node
    def delete(self,data):
        if self.root:
            self.__remove(data,self.root)
    
    def __remove(self,data,node):
        if not node:
            return None
        if data<node.data:
            node.leftChild=self.__remove(data,node.leftChild)
        elif data>node.data:
            node.rightChild=self.__remove(data,node.rightChild)
        elif data == node.data:
            if not node.leftChild and not node.rightChild:
                # print('Removing leaf node')
                del node
                return None
            elif not node.leftChild:
                tempNode=node.rightChild
                del node
                # print('Removing node with 1 child')
                return tempNode
            elif not node.rightChild:
                tempNode=node.leftChild
                del node
                # print('Removing node with 1 child')
                return tempNode
            else:
                # print('Removing node with 2 child')
                tempNode=self.__predecessor(node.leftChild)
                node.data=tempNode.data
                node.leftChild=self.__remove(tempNode.data,node.leftChild)
        if not node:
            return node
        node.height=max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) +1
        balanced=self.checkBalanced(node)

        #double left heavy
        if balanced>1 and self.calcHeight(node.leftChild)>=0:
            print('Right right rotation')
            return self.rightRotate(node)
            
        #double right heavy
        if balanced<-1 and self.calcHeight(node.rightChild)<=0:
            print('Left left rotation')
            return self.leftRotate(node)
        
        # left right heavy
        if balanced>1 and self.calcHeight(node.rightChild)<0:
            print('Left right rotation')
            node.leftChild=self.leftRotate(node.leftChild)
            return self.rightRotate(node)

        # right left heavy
        if balanced<-1 and self.calcHeight(node.leftChild)>0:
            print('Right left rotation')
            node.rightChild=self.rightRotate(node.rightChild)
            return self.leftRotate(node)
        return node    
    
    # Finds the predecessor node
    def __predecessor(self, root):
        if root.rightChild:
            return self.__predecessor(root.rightChild)
        return root


    # RIGHT Rotate (left heavy)
    def rightRotate(self,node):
        print('rotating the root to right',node.data)
        tempLeft=node.leftChild
        t=tempLeft.rightChild

        tempLeft.rightChild=node
        node.leftChild=t
        
        node.height=max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) +1
        tempLeft.height=max(self.calcHeight(tempLeft.leftChild) , self.calcHeight(tempLeft.rightChild)) +1
        return tempLeft

    # LEFT Rotate (right heavy)
    def leftRotate(self,node):
        print('rotating the root to left',node.data)
        tempRight=node.rightChild
        t=tempRight.leftChild

        tempRight.leftChild=node
        node.rightChild=t
        
        node.height=max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) +1
        tempRight.height=max(self.calcHeight(tempRight.leftChild) , self.calcHeight(tempRight.rightChild)) +1
        return tempRight

    # print the avlTree
    def printTree(self):
        if self.root:
            self.traverseInoder(self.root)
    
    def traverseInoder(self,root):
        if root.leftChild:
            self.traverseInoder(root.leftChild)
        
        print(root.data)

        if root.rightChild:
            self.traverseInoder(root.rightChild)

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
    def pirntRoot(self):
        print(self.root.data,'is the root')
avl=avlTree()

avl.insert(1)
avl.insert(5)
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(60)
avl.insert(70)
avl.insert(80)
avl.insert(90)
avl.printTree()
print(avl.search(10))
print('After deleting')
avl.delete(60)
avl.delete(50)
avl.printTree()
avl.pirntRoot()
