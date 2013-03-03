uidaho-cs470-connectfour
========================
Project: Write a program to play Connect Four against a human opponent.

Requirements: The program must use a minmax search algorithm. The user must be able to determine which side goes first. The program must display the board after each move. (This can be a simple text based display.) The program must not take more than 30 seconds to make a move.

Algorithms: Your program must use, at least, minmax search. You will need to write an evaluation heuristic because searching the entire game tree is not feasible. Your heuristic must weigh wins and losses so that the program always blocks a potential win by the opponent (if there are three opponent pieces in a row the computer places a piece to block the win) and always makes a winning move if one is available. Note: if there are two possible paths to a sure victory the program may take the longer one.

Scoring: The project will be scored out of 200. Just a minmax search algorithm is worth up to 160 points. The additional 40 points are for including additional, algorithmic techniques: alpha-beta pruning, selective evaluation, etc.

I plan to arrange a Connect Four tournament, with the programs playing against each other. Thus, the time limit and ability to go first or second is important.

Hand-In:

You need to hand in typed write-up containing the following:
* An abstract summarizing what you did and what the results were.
* An introduction explaining game playing in general and connect four specifically.
* An algorithm section explaining your program. Including,
    * A description of the major data structures.
    * The details of the search algorithm used: minmax, alpha-beta pruning, selective evaluation, maximum search depth, etc.
    * The evaluation function used.
* A results section. Including,
    * Samples of the program's output. An entire game is not required, but you should include examples of the programming blocking a win and taking a win.
    * A discussion of how the program behaved. Did it have any strengths or weaknesses?
* A conclusion section.
