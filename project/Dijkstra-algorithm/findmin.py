#You are to write a function "find_min(color, queue)" that takes a vertex-coloring and a list of vertices, 
#and returns a vertex in the list, whose color is smallest.
def find_min(color,queue):
    result = ""
    min = color[queue[0]]
    for i in queue:
        if color[i] <= min:
            min = color[i]
            result = i
    return result
