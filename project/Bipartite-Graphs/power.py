#In the cell below, you are to write a function "power(list)" that takes in a list as its input, 
#and then returns the power set of that list. You may assume that the input will not have any duplicates (i.e., it's a set).
def power(list):
    listLength = len(list)
    powerSet = []
    for i in range(1 << listLength):
        powerSet.append([list[j] for j in range(listLength) if (i & (1 << j))])
    print (powerSet)
