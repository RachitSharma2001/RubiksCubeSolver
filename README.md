# RubiksCubeSolver
A Python program that is inputed a Rubiks Cube configuration and outputs the moves necessary to solve it. Uses AStar algorithm.

In this program, I implemented the A star heuristic search algorithm to solve a given Rubik's cube configuration.

The way A star works is that it starts at a certain point, and runs a greedy search algorithm where it visits states that have the lowest estimated
total length to the goal state. This estimated length is the current distance traveled to point + estimated length to destination from point. 

The latter is calculated using an heuristic function. I created a rather simple heuristic function: it just adds all individual face's distances from the 
side their colors should be on.
