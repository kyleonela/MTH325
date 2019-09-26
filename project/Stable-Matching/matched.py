#In the cell below, you are to write a function called "matched(dic)" that takes in a dictionary and 
#returns the boolean value False if any key is exactly '[]', and returns True otherwise.
def matched(dic):
    for val in dic:
        if(dic[val]==[]):
            return False
    return True
