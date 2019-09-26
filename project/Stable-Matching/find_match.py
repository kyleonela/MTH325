#In the cell below, you are to write a function "find_match(dic, fam)" that takes in a dictionary and value 'fam', 
#and returns the key for which fam is the value. 
#If 'fam' is NOT the value of any key, then the method should return [].
def find_match(dic,fam):
    lst = []
    
    for x in dic:
        if(fam in dic[x]):
            #lst.append(x)
            return x
    #print (lst)
