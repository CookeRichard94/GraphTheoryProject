# Richard Cooke
# G00331787@gmit.ie

# Graph Theory Project
# The Purpose of this Project is to create a Python script that can
# build a non-deterministic finite automaton (NFA) from a regular expression
# and use the NFA to check if the regular expression matches any given
# string of text

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
 
    #
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

# Potential test cases to check if the Shunting yard 
# Algorithm is running without fault
#expected output should be ab.c*d.|
print (shntYrdAlg("(a.b)|(c*.d)"))
#expected output should be abc*.cd*|
print (shntYrdAlg("(a.*b)|(c*d)"))
#expected output should be ab*cd.|
print (shntYrdAlg("(a*b)|(c.d)"))


#Thompson's Construction

#Each one reperesents a state that has two arrows
#None is used for a label to represent an empty set for the arrows
class state:
    label, arrow1, arrow2 = None, None, None

# Each NFA contains and intial and an accept state
class nfa:
    initial, accept = None, None

    def __init__(self, initial, accept):
        self.initial, self.accept = initial, accept

def compile(pofix):
    nfaStack = []

    for c in pofix:
        if c == '*':
            #Pops a single NFA from the stack
            nfa1 = nfaStack.pop()
            #Creates new initial and accept states for the new NFA
            accept, initial = state(), state()
            #Joins the new accept state to the accept state of nfa1 and the new 
            #initial state to the initial state of nfa1
            initial.arrow1, initial.arrow2 = nfa1.initial, accept
            #Joins the old accept state to the new accept state and to nfa1's intial state
            nfa1.accept.arrow1, nfa1.accept.arrow2 = nfa.initial, accept
            #Pushes the new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '.':
            #Pops 2 NFA's off the stack
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            #Connects first NFA's accept state to the second NFA's 
            #Initial state
            nfa1.accept.arrow1 = nfa2.initial
            #Pushes the new NFA to the stack
            nfaStack.append(nfa1.initial, nfa2.accept))
        elif c == '|':
            #Pops 2 NFA's off the stack
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            #Creates a new initial state 
            initial = state()
            #Connects the new initial state to the two NFA's that have been
            # popped from the stack
            initial.arrow1, initial.arrow2 = nfa1.initial, nfa2.initial
            #Creates a new Accept state
            accept = state()
            #Connects the new Accept state to the two NFA's popped from the stack
            nfa1.accept.arrow1, nfa2.accept.arrow1 = accept, accept
            #Pushes the new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '+':
            #Pops a single NFA from the stack
            nfa1 = nfaStack.pop()
            #Creates new initial and accept states for the new NFA
            accept, initial = state(), state()
            #Joins the new initial state to the initial state of nfa1
            initial.arrow1 = nfa1.initial
            #Joins the old accept state to the new accept state and to nfa1's intial state
            nfa1.accept.arrow1, nfa1.accept.arrow2 = nfa.initial, accept
            #Pushes the new NFA to the stack
            nfastack.append(nfa(initial, accept))
        else:
            #Creates new accept and initial states
            accept, initial = state(), state()
            #Joins the initial state to the accept state using an arrow that is labbelled c
            initial.label, initial.arrow1 = c, accept
            ##Pushes the new NDA to the stack
            nfastack.append(nfa(initial, accept))
