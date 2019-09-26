#In the cell below, you are to write a function "partite_sets(graph)" that takes in a BIPARTITE graph as its input, 
#and then returns a single list whose two entries are the partite sets of the graph as lists 
#(the order of the sets outputed does not matter).
def partite_sets(graph):
    setX=[]
    setY=[]
    
    for firstVal in graph:
        setX.append(firstVal)
        break
        
    for v in graph:
        if v in setX:
            for y in graph[v]:
                if y not in setY:
                    setY.append(y)
        else:
            for x in graph[v]:
                if x not in setX:
                    setX.append(x);
                    
    partiteSet = []
    partiteSet.append(setX)
    partiteSet.append(setY)
    return partiteSet
