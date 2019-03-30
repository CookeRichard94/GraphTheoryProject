# Richard Cooke
# G00331787@gmit.ie

Graph Theory Project
The Purpose of this Project is to create a Python script that can build a non-deterministic finite automaton (NFA) from a regular expression and use the NFA to check if the regular expression matches any given string of text

This repository was developed as part of the Graph Theory Module of 3rd Year Software Development in GMIT.

To download the repository enter to the command line and cd into an appropriate file, then run the command 'git clone https://github.com/CookeRichard94/GraphTheoryProject'. From there cd into the the downloaded folder. To run the script run the code 'python project.py'. Test cases within the script can be modified to test each operator as instructed in the comments.

=======================================
          ShntYrdAlg Function
=======================================
The purpose of this method is to parse an infix regular expression into postfix. This is done using Dijkstra's Shunting-Yard Algorithm. First, a series of special characters '*', '+', '?', '.', '|' are added to a python library, with each character being given a value to signify the order of precedence for each character. A for loop is then used to run through the infix expression that has been passed to the method as a parameter. character by character. A series of if statements are then used inside the loop to determine the output for the postfix expression.

The first if is used if a '(' is encountered. If so, then the '(' is sent to the stack. The next if handles whether the character is = ')'. If so, the stack is looped until '(' is found, until it is found each item on the stack is added to the postfix and the stack is then shortened.
The next if check if the character is in the specialChars library. If so, the stack is looped while the precedence of the current character is lower than the character at the top of the stack, the last character on the stack is added to the postfix and the stack is shortened and eventually the character checked is added to the stack.
If none of these conditions are met then the current character is appended to the postfix.

The accumulated postfix expression is then returned from the function as a string.

=======================================
          Compile Function
=======================================
The Compile function parses the postfix expression that was attained from the ShntYrdAlg function and uses it to create a Non-Deterministic Finite Automata(NFA) based on the postfix sent in it's parameter. The core of this function is based on Thompson's construction. (https://www.youtube.com/watch?v=RYNN-tb9WxI) A helpful video for understanding what an NFA is.
First, two classes are created to assist with this function, an nfa class and a state class. The state class contains three variables(label, arrow1, arrow2) all of which are assigned the None value. The nfa class contains two variables(accept, initial) both of which are assigned the None value and also a constructor.

In the function, first an empty set called nfaStack is created. Next a for loop is used to loop through the postfix character by character before breaking off into individual if statements for each possible outcome. 
The first if deals with the '*' character. If so, an NFA is popped from the stack, called nfa1 and a new initial and accept state are created. The new accept state is joined to the the accept state of nfa1 and the new initial state is joined to the initial state of nfa1. The old accept state is then joined to the new accept state and so is the initial. The new nfa is then appended to the nfaStack.
The next if deal with the '.' character. If so, then two NFA's are popped from the stack, called nfa1 and nfa2. Then the accept state of nfa1 is connected the initial state of nfa2 and the new nfa is appended to the nfaStack.
The next if deals with the '|' character. If so, then two NFA's are pooped from the stack, called nfa1 and nfa2. A new initial and accept state are then created. The initial states of nfa1 and nfa2 are connected to the new initial state. The new accept state is then connected to the accept states of nfa1 and nfa2. the new NFA is then appended to the nfaStack.
The next if deals with the '+' character. If so, then a single NFA called nfa1, is popped from the stack. A new initial and accept state are created. The initial state of nfa1 is then connected to the initial state. The old accept state is then joined to the new accept state and so is the initial. The new nfa is then appended to the nfaStack.
The next if deals with the '?' character. If so, then a a single NFA called nfa1 is popped from the stack. A new accept and initial state are created. The new accept state is joined to the the accept state of nfa1 and the new initial state is joined to the initial state of nfa1. The old accept state is then joined to the new accept state. The new NFA is then appended to the nfaStack.
If none of the special characters are met then the else statement is called. In this case a new accept and intial state are created. The initial state is then connected to the accept state using an arrow that has been labelled using the character in question. The new NFA is then appended to the nfaStack.

=======================================
          Followes Function
=======================================




=======================================
          MatchString Function
=======================================












=======================================
               Research
=======================================
