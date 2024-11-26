Project Description
This project is an implementation of the Tuple Out Dice Game, 
where two players take turns rolling three dice. The objective
is to score the most points, or to be the first to reach 50 points.
During each player's turn, they can re-roll any dice that are not
"fixed," but if they roll three of the same number (a "tuple"),
they score zero for that turn.

Game Rules:
The player rolls three dice.
If all three dice have the same value (a "tuple"), the player gets
zero points for that turn.
If two dice are the same, those dice are "fixed" and cannot be re-rolled.
The player can re-roll the dice that are not "fixed" until they decide to
stop, or until they "tuple out."
The player scores the sum of the dice at the end of their turn, unless
they "tuple out," in which case they score zero.
The game ends when a player reaches 50 points or when both players decide
to stop playing.

Included Features
Two-player mode: The game is designed for two players. Each player takes
turns rolling the dice and re-rolling as needed.
Tuple out rule: If a player rolls three identical dice, their turn ends
with zero points.
Re-roll mechanic: Players can re-roll dice that are not fixed (i.e., not
part of a pair).
Score tracking: The game keeps track of each player's score, and displays
the running totals throughout the game.

Game Requirements:
Python 3

How to Run the Program
1. Install Python 3
2. Navigate to the Project Folder
Once the project is downloaded, navigate to the project folder in your
terminal or command prompt:
ie: cd Downloads -->
cd INST126 -->
cd INST126_consolidation -->
python3 INST126_consolidationproject.py

4. Run the Game
To start the game, run the following command in your terminal:
python3 INST126_consolidationproject.py

5. Gameplay
The game will prompt each player to roll the dice and decide whether
to re-roll the non-fixed dice.
The game will continue until one player reaches 50 points.

Example Gameplay
Welcome to the Tuple Out Dice Game!
The first player to reach 50 points wins!

Player 1's turn!
Initial roll: [2, 4, 4]
Fixed dice: [4, 4]
Re-roll unfixed dice? (y/n): y
Re-rolled dice: [4, 4, 3]
Player 1 scores 11 points.
Current scores: {'Player 1': 11, 'Player 2': 0}

Player 2's turn!
Initial roll: [3, 3, 3]
Tuple out! No points for this turn.
Current scores: {'Player 1': 11, 'Player 2': 0}

Notes:
This implementation currently supports only two players.
The game ends when a player reaches 50 points.