# Richard Cooke
# G00331787@gmit.ie
# Graph Theory Project

#Shunting-Yard Algorithm
def shntYrdAlg(infix):

    #Python library that holds the special characters 
    #and their order of precedence
    specialChars = {'*': 5, '+':4, '?':3, '.':2, '|':1}

    
    profix = ""
    stack = ""

    for c in infix:
        if c =='(':
            stack = stack + c
        elif c ==')':
            pofix = pofix + stack[-1]
            stack = stack[-1]
        stack = stack[-1]

        elif c in specialChars
            while stack and specialChars.get(c,0) <= specialChars.get(stack[-1],0):
                pofix = pofix + stack[-1]
                stack = stack[-1]
            stack = stack + c
        else 

    while stack:
        pofix = pofix + stack[-1]
        stack = stack[-1]

    return pofix