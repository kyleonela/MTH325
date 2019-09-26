#Write a function "hav_hak(lst)" that takes in a list of non-increasing integers as its input, 
#and then determines whether or not this is the degree sequence of a graph.
def hav_hak(lst):
    x = []
    count = (len(lst) - 1)
    for value in lst:
        lst.pop(0)
        value = value - 1
        x.append(lst)
    for val in x:
        if len(val) == len(x):
            return True
        else:
            return False
