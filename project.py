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
    specialChars = {'*': 25, '+': 20, '?': 15, '.':10, '|':5}
    # * = 0 or more
    # + = 1 or more
    # ? = 0 or 1
    # . = concatenate
    # | = or
 
    #postfix and stack are initially created as empty strings
    #the stack is used to temporarily hold characters to be pushed to the pofix
    #The pofix is used as the output for the Shunting yard algorithm
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
            #while loop that runs while the last character on the stack is not a (
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]
        # if the character at c is in the specialChars library and it's prcedence 
        # is lower <= to the last chaarcter in the stack, then pop 
        elif c in specialChars:
            #while loop that runs while the current special character has a lower
            #precedence than the special character on the stack
            while stack and specialChars.get(c, 0) <= specialChars.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        #
        else:
            pofix = pofix + c

    #
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]

    #returns the corrected regular expression in postfix
    return pofix

# Potential test cases to check if the Shunting yard 
# Algorithm is running without fault
#expected output should be ab.c*d.|
#print (shntYrdAlg("(a.b)|(c*.d)"))
#expected output should be abc*.cd*|
#print (shntYrdAlg("(a.*b)|(c*d)"))
#expected output should be ab*cd.|
#print (shntYrdAlg("(a*b)|(c.d)"))


#Thompson's Construction
#https://cs.stackexchange.com/questions/76488/thompsons-construction-transforming-a-regular-expression-into-an-equivalent-nf

#Each one reperesents a state that has two arrows
#None is used for a label to represent an empty set for the arrows
class state:
    #Variables for the state class
    #None is used in python as a way of saying the the value of a variable has not been assigned yet
    label, arrow1, arrow2 = None, None, None

# Each NFA contains and intial and an accept state
class nfa:
    #Variables in the nfa class
    initial, accept = None, None 

    #constructor for building a new nfa
    def __init__(self, initial, accept):
        self.initial, self.accept = initial, accept

#Method that takes in a regular expression and turns them into a 
#data structure(NFA)
# https://www.youtube.com/watch?v=RYNN-tb9WxI A helpful video for understanding NFA's
def compile(pofix):
    nfaStack = []

    for c in pofix:
        if c == '*':
            #Pops a single NFA from the stack
            nfa1 = nfaStack.pop()
            #Creates new initial and accept states for the new NFA
            initial, accept = state(), state()
            #Joins the new accept state to the accept state of nfa1 and the new 
            #initial state to the initial state of nfa1
            #Accept connected to inital because empty is acceptable
            initial.arrow1, initial.arrow2 = nfa1.initial, accept
            #Joins the old accept state to the new accept state and to nfa1's intial state
            nfa1.accept.arrow1, nfa1.accept.arrow2 = nfa1.initial, accept
            #Pushes the new NFA to the stack
            nfaStack.append(nfa(initial, accept))
        elif c == '.':
            #Pops 2 NFA's off the stack
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            #Connects first NFA's accept state to the second NFA's 
            #Initial state
            nfa1.accept.arrow1 = nfa2.initial
            #Pushes the new NFA to the stack
            nfaStack.append(nfa(nfa1.initial, nfa2.accept))
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
            nfaStack.append(nfa(initial, accept))
        elif c == '+':
            #Pops a single NFA from the stack
            nfa1 = nfaStack.pop()
            #Creates new initial and accept states for the new NFA
            accept, initial = state(), state()
            #Joins the new initial state to the initial state of nfa1
            initial.arrow1 = nfa1.initial
            #Joins the old accept state to the new accept state and to nfa1's intial state
            nfa1.accept.arrow1, nfa1.accept.arrow2 = nfa1.initial, accept
            #Pushes the new NFA to the stack
            nfaStack.append(nfa(initial, accept))
        elif c == '?':
            #Pops a single NFA from the stack
            nfa1 = nfaStack.pop()
            #Creates new initial and accept states for the new NFA
            accept, intial = state(), state()
            #Joins the new accept state to the accept state of nfa1 and the new 
            #initial state to the initial state of nfa1
            #Accept connected to inital because empty is acceptable
            initial.arrow1, initial.arrow2 = nfa1.initial, accept
            #
            nfa1.accept.arrow1 = accept
            #Pushes the new NFA to the stack
            nfaStack.append(nfa(initial, accept))
        else:
            #Creates new accept and initial states
            accept, initial = state(), state()
            #Joins the initial state to the accept state using an arrow that is labbelled c
            initial.label, initial.arrow1 = c, accept
            ##Pushes the new NDA to the stack
            nfaStack.append(nfa(initial, accept))
        
    #Should only have a single NFA
    return nfaStack.pop()

#expected output is a .nfa at a specified memory location
#print(compile("ab.cd.|"))
#print(compile("aa.*"))

# https://swtch.com/~rsc/regexp/regexp1.html
#Returns the states that can be reach by following the arrows
def followes(state):
    # Creates new set, with state as the only member
    states = set()
    states.add(state)

    #Check if any of the arrows are labelled empty
    if state.label is None:
        #Checks if arrow1 is a state
        if state.arrow1 is not None:
            #Follows arrow1
            states |= followes(state.arrow1)
        #Checks of arrow2 is a state
        if state.arrow2 is not None:
            #Follows arrow2
            states |= followes(state.arrow2)

    #Returns the set of states
    return states

#Matches a string to an infix regular expression
def matchString(infix, string):
    #Shunt and compile the infix
    postfix = shntYrdAlg(infix)
    nfa = compile(postfix)

    #Current set of states and next set of states
    currentState = set()
    nextState = set()

    #Adds the initial satte to the current set
    currentState |= followes(nfa.initial)

    #For loop to loop through each character in the string one by one
    for s in string:
        #For loop to loop through tbe currentState
        for c in currentState:
            #checks if the state is labbeled s
            if c.label == s:
                #Adds arrow1 to the next set
                nextState |= followes(c.arrow1)
        #sets the currenState to next and clears out the nextState
        currentState = nextState
        nextState = set()
    
    #Checks if the accept state is in the set for current state
    return (nfa.accept in currentState)

#Testcases for the matchString function
#infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
#strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

#Running test from Matching by hand video
infixes = ["(a.a)?"]
strings = ["", "a", "aa", "aaa", "aaaa"]

for i in infixes:
    for s in strings:
        print(matchString(i,s),i,s)
