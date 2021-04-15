class TreeNode():
    def __init__(self,char):
        self.char=char
        self.children={}
        self.endWhere= False
    
class Trie():
    def __init__(self):
        self.root=TreeNode(None)
    
    def insert(self,word):
        parent=self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char]=TreeNode(char)
            parent=parent.children[char]
        if i==len(word)-1:
            parent.endWhere=True
    
    def search(self,word):
        parent=self.root
        for char in word:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return parent.endWhere
    
    def startsWith(self,prefix):
        parent=self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return True

# Main function
trie=Trie()
trie.insert('apple')
trie.insert('app')
trie.insert('applet')
trie.insert('apt')

print(trie.search('apple'))
print(trie.search('app'))
