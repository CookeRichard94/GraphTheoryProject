# Richard Cooke
# G00331787@gmit.ie
# Graph Theory Project

#Shunting-Yard Algorithm
#https://brilliant.org/wiki/shunting-yard-algorithm/
def shntYrdAlg(infix):

    #Python library that holds the special characters 
    #and their order of precedence
    specialChars = {'*': 25, '+':20, '?':15,'.':10, '|':5}
    # * = 0 or more
    # * = 1 or more
    # ? = 
    # . = concatenate
    # | = or
 
    pofix, stack = "", ""

    # For loop to loop through each character
    # of the infix string one by one
    for c in infix:
        #If the character at c is an ( then add it to the stack
        if c =='(':
            stack = stack + c
        #if the character at c is an ) and while the last character on the stack
        # is not a ( then pop everything from the stack on to the pofix
        # otherwise 
        elif c ==')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]
        # if the character at c is in the specialChars library and it's prcedence 
        # is lower <= to the last chaarcter in the stack, then pop 
        elif c in specialChars:
            while stack and specialChars.get(c, 0) <= specialChars.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]

    return pofix

#
print (shntYrdAlg("(a.b)|(c*.d)"))
print (shntYrdAlg("(a.*b)|(c*d)"))
print (shntYrdAlg("(a*b)|(c.d)"))


#Thompson's Construction
#
class state:
    label, arrow1, arrow2 = None, None, None

#
class nfa:
    initial, accept = None, None

    def __init__(self, initial, accept):
        self.initial, self.accept = initial, accept

def compile(pofix):
    nfaStack = []

    for c in pofix:
        accept, initial = state(), state()
        initial.label = c

        if

        elif

        elif

        else
