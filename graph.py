from collections import deque

# Create a Graph class
class Graph():
    
    # Initialize Nodes list and Adajency list
    def __init__(self,isdirected=False):
        self.nodes=[]
        self.adjlist={}
        self.isdirected=isdirected
    
    # Adds vertex to the graph
    def addVertex(self,vertex):
        self.nodes.append(vertex)
        self.adjlist[vertex]=[]
    
    #Add Edge to the graph
    def addEdge(self,u,v):
        self.adjlist[u].append(v)
        if not self.isdirected:
            self.adjlist[v].append(u)
    
    # Delete vertex and its edges from the graph
    def deleteVertex(self,vertex):
        self.nodes.remove(vertex)
        if not self.isdirected:
            for node in self.adjlist[vertex]:
                self.adjlist[node].remove(vertex)
            del self.adjlist[vertex]
            return
        else:
            del self.adjlist[vertex]
            for node in self.adjlist.keys():
                try:
                    self.adjlist[node].remove(vertex)
                except:
                    pass
            return

    # Delete the edge    
    def deleteEdge(self,u,v):
        self.adjlist[u].remove(v)
        if not self.isdirected:
            self.adjlist[v].remove(u)
    
    # Prints the degree of the vertex
    def degree(self,vertex):
        print(f'{len(self.adjlist[vertex])} is the degree of {vertex}')
    

    # BFS --> Queue
    def bfs(self,startVertex):
        queue=deque()
        visited=set()
        queue.append(startVertex)
        visited.add(startVertex)

        while queue:
            acutualVertex=queue.popleft()
            print(acutualVertex)
            for u in self.adjlist[acutualVertex]:
                if u not in visited:
                    queue.append(u)
                    visited.add(u)
        print()

    # DFS --> Recursion
    def dfs(self,startVertex,visited=set()):
        visited.add(startVertex)
        print(startVertex)
        for n in self.adjlist[startVertex]:
            if n not in visited:
                visited.add(n)
                self.dfs(n,visited)


    # Prints the graph
    def printGraph(self):
        for node in self.adjlist:
            print(f'{node} --> {self.adjlist[node]}')
        print()

#Main function
graph=Graph(False)

#add vertices
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')

#add edges
graph.addEdge('a','b')
graph.addEdge('a','c')
graph.addEdge('b','c')
graph.addEdge('c','d')
graph.addEdge('b','d')
graph.addEdge('d','e')
graph.addEdge('a','d')

#play with the methods
graph.printGraph()
# graph.deleteEdge('c','d')
# graph.deleteVertex('b')
graph.printGraph()
graph.degree('f')

graph.bfs('a')
graph.dfs('c')