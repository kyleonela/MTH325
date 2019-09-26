#In the cell below, you are to write a function called "get_nhbr(lst, graph)" that takes in two inputs: a list of vertices and a graph. 
#The function is to return a list that contains the neighborhood of the vertices in 'lst' 
#(remember that this means you are finding the union of the individual vertices' neighborhoods).
def get_nhbr(lst,graph):
    neighborhood = []
    for key in graph:
        for val in lst:
            if val in graph[key] and key not in neighborhood:
                    neighborhood.append(key)
    return neighborhood
