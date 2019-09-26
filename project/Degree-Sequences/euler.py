#Write a function "euler(graph)" that takes in a connected graph as its input, and then determines if it is Eulerian or not.
def euler(graph):
    degree = deg_seq(graph)
    for d in degree:
        if(degree[d]%2 == 0):
            return True
        else:
            return False
