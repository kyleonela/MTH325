#You are to write a function has "perfect(graph)" that takes in a BIPARTITE graph as its input, 
#and then determintes whether or not the graph has a perfect matching. 
#In other words, it will return the Boolean value True if it has one, and False if it does not.
def has_perfect(graph):
    pSet = partite_sets(graph)
    setX = pSet[0]
    setY = pSet[1]
    
    for x in graph:
        if x in setX:
            if graph[x] != setY:
                return False
        else:
            if graph[x] != setX:
                return False
            
    return True
