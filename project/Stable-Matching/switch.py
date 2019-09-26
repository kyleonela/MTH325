#In the cell below, you are to write a function "switch(pref, dog, fam, cur_dog)" that takes in a preference list 'pref' 
#(in which 'fam' is a key), along with three objects 'dog', 'fam', and 'cur_dog'. 
#This method should return the boolean value True if 'fam' prefers (based on the preference list 'pref') 'dog' over 'cur_dog', 
#and return False otherwise.
def switch(pref,dog,fam,cur_dog):
    #does this fam like dog over cur dog
    
    lst = []
    for val in pref:
        if fam in val:
            lst.append(pref[val])
    for value in lst:
        if(value.index(cur_dog) < value.index(dog)):
            return False
        else:
            return True
