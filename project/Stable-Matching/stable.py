#In the cell below, you are to write a function "stable(pref1, pref2)" that takes in two preference lists 
#(say one for dogs and the other for families), and returns a stable matching (in the form of a dictionary).
import copy

def stable(pref1, pref2):
    dog = sorted(pref1.keys())
    fam = sorted(pref2.keys())
    key = dog[:]
    keys = fam[:]
    pref = copy.deepcopy(pref1)
    pre = copy.deepcopy(pref2)
    stab = {}
    
    while key:
        v = key.pop(0)
        match = pref[v]
        f = match.pop(0)
        perf = stab.get(f)
        if not perf:
            stab[f] = v
        print (stab)
