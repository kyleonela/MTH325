#You are to write a function "initial(graph, source)" that takes in a weighted graph and a vertex as its input 
#and returns a vertex-coloring in which the 'source' is colored with 0 and all other vertices are colored with 'infty'.
def initial(graph, source):
    seq = {}
    for i in graph:
        seq[i] = infty(graph)
    seq[source] = 0
    return seq
