#You are to write a function "deg_seq(graph)" that takes in a graph as its input, 
#and then returns the degree sequence of the graph as a list.
def deg_seq(graph):
    edge = []
    degree = []
    for vert in graph:
        edge.append(graph[vert])
    for e in edge:
        degree.append(len(e))
    degree.sort(reverse = True) 
    return degree 
