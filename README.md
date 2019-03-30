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
The purpose of this function is to tell the program which states can be reached by following the arrows attached to each NFA. First, a new set is created with state as the the only member. Then an if statement checks if the label attached to the state has not been assigned a value yet. If label is still = None then two nested if statements are used to check if arrow1 and arrow 2 of the state are not None, if so, then the arrows can be followed and the state is returned by the function.      

=======================================
          MatchString Function
=======================================
The MatchString function matches a string to an infix regular expression. The method is passed two parametres, an infix expression and the string that is to be matched against the infix. The MatchString function essentially acts as the scripts main method.

First, the ShntYrdAlg function is called and fed the infix as it's parameter, the postfix that is returned from the ShntYrdAlg is then fed to the compile method as it's paramter. Next to state sets are created called, currentState and nextState.Then the initial state is added to the current state by calling the the followes function and passing it the initial state as it's parameter.

Next a for loop reads through the input string character by character, then an inner for loop is used to loop through the currentState and uses an if statement to check if the label attached to the current state is equal to the current character on the outer for loop. If this is true then arrow1 is added to the next set by calling the followes function and passing it the NFA's arrow1 as a paramter. At the end of the outer for loop the currentState is set to the newState and the newState is cleared. 

The function then returns when it confirms that the accept state for the NFA is located within the currentState.


At the end of each function, potential test cases are provided in commented code to test whether the function has the correct output.

=======================================
               Research
=======================================
The plan of approach for this project, that I undertook was to complete the process over 3 weeks. The first two weeks would be dedicated to trying to understand the task at hand and get a grasp of what was being asked before viewing the provided video material. Then the final week was to be used to complete the coding and documentation side of the project.

I found this approach to be helpful in coming to understand the project itself as I entered this module without any prior python coding experience and the knowledge attained in preparation for the coding to have greatly sped up the process. However I did find that, through just reading material on the conetent, I was often left confused by what was being described and did not feel like I had grasped a firm understanding on the concept of using NFA's until I combined the learned material with the provided "by hand" videos provided for the module. To ammend the initial struggle with understanding the content, ideally I would intergrate the videos into the reading process earlier than I did.

Prior to viewing the videos provided, the biggest help in understanding the project was viewing similarly coded projects that where created using other programming languages such as java.

Links to some of the material I used to research the project before starting:
https://www.youtube.com/watch?v=RYNN-tb9WxI
https://swtch.com/~rsc/regexp/regexp1.html
https://www.cs.york.ac.uk/fp/lsa/lectures/REToC.pdf
https://brilliant.org/wiki/shunting-yard-algorithm/
http://www.oxfordmathcenter.com/drupal7/node/628
https://www.javatpoint.com/java-regex
