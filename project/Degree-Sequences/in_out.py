#Write a function "in_out(digraph, vert)" that takes in a directed graph and a vertex as its input, 
#and then returns the in-degree and out-degree of that vertex in the directed graph in the form of a 
#list with rst entry as the in-degree and second entry as the out-degree.
def in_out(digraph, vert):
    outD = 0
    inD = 0
    degree = []
    for v in digraph:
        if v == vert:
            outD = len(digraph[v])
        if vert in digraph[v]:
            inD += 1
    degree.append(inD)
    degree.append(outD)
    
    return degree
