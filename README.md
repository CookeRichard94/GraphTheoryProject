# Richard Cooke
# G00331787@gmit.ie

Graph Theory Project
The Purpose of this Project is to create a Python script that can build a non-deterministic finite automaton (NFA) from a regular expression and use the NFA to check if the regular expression matches any given string of text

This repository was developed as part of the Graph Theory Module of 3rd Year Software Development in GMIT.

To download the repository enter to the command line and cd into an apporpriate file, then run the command 'git clone https://github.com/CookeRichard94/GraphTheoryProject'. From there cd into the the downloaded folder. To run the script run the code 'python project.py'. Test cases within the script can be modified to test each operator as insctructed in the comments.

============================================
           ShntYrdAlg Function
============================================
The purpose of this method is to parse an infix regular expression into postfix. This is done using Dijkstra's Shunting-Yard Algorithm. First, a series of special characters '*', '+', '?', '.', '|' are added to a python library, with each characetr being given a value to signify the order of precendece for each character. A for loop is then used to run through the infix expression that has been passed to the method as a paramter. chracter by character. A series of if statements are then used inside the loop to determine the output for the postfix expression.

The first if is used if a '(' is encountered. 
