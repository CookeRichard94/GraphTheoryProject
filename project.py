# Richard Cooke
# G00331787@gmit.ie
# Graph Theory Project

#Shunting-Yard Algorithm
#https://brilliant.org/wiki/shunting-yard-algorithm/
def shntYrdAlg(infix):

    #Python library that holds the special characters 
    #and their order of precedence
    specialChars = {'*': 5, '+':4, '?':3, '.':2, '|':1}
    # * = 0 or more
    # * = 1 or more
    # ? = 
    # . = concatenate
    # | = or
 
    pofix = ""
    stack = ""

    # For loop to loop through each character
    # of the infix string one by one
    for c in infix:
        if c =='(':
            stack = stack + c
        elif c ==')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[-1]
            stack = stack[-1]
        elif c in specialChars:
            while stack and specialChars.get(c,0) <= specialChars.get(stack[-1],0):
                pofix, stack = pofix + stack[-1], stack[-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[-1]
    stack = stack[-1]

    return pofix

print (shntYrdAlg("(a.b)|(c*.d)"))
print (shntYrdAlg("(a.*b)|(c*d)"))
print (shntYrdAlg("(a*b)|(c.d)"))