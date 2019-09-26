#You are to write a function "dijkstra(graph, source)" that takes in a weighted graph and a vertex as its input 
#and returns a 'vertex-coloring' in which each vertex is labelled with the shorest, 
#weighted distance possible from the 'source'. (Note that you are not to keep track of the parents in this version).
def dijkstra(graph, source):
    working = initial(graph, source)
    queue = []
    for i in graph:
        queue.append(i)
    while len(queue) != 0:
        currSource = find_min(working, queue)
        queue.remove(currSource)
        step = working[currSource]
        for j in queue:
            edgeWeight = -1
            for k in graph[currSource]:
                if k[0] == j:
                    edgeWeight = k[1]
                    break
            if edgeWeight != -1:
                cand = step + edgeWeight
                if working[j] > cand:
                    working[j] = cand
    return working
