#In the cell below, you are to write a function "is_bipartite(graph)" that takes in a graph as its input, 
#and then determines whether or not the graph is bipartite. In other words, it returns True if it is, and False if it is not.
def is_bipartite(graph):
    pSet = partite_sets(graph)
    setX = pSet[0]
    setY = pSet[1]
    
    for x in setX:
        if x in setY:
            return False
        else:
            return True
