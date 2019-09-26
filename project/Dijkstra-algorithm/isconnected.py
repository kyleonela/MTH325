#You are to write a function "is_connected(graph)" that takes in a weighted graph as its input and determines
#whether or not the graph is connected.
def is_connected(graph):
    verts = []
    for key in graph:
        verts.append(key)
    conn_test = dijkstra(graph, verts[0])
    inf = infty(graph)
    for i in conn_test:
        if conn_test[i] == inf:
            return False
    return True
