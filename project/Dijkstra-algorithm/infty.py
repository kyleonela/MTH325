# You are to write a function "infty(graph)" that takes in a weighted graph as its input and returns the sum of all the edge-weights plus 1.
def infty(graph):
    weight = 0
    for i in graph:
        for j in graph[i]:
            weight += j[1]
    return (weight/2) +1
