# Python-Game

Python Project Documentation

Team Name: Karan Khanna
Team Member: Karan Khanna 

Python Project Title: Space Invader Game

Project Overview:
This project is a simple ASCII-based "Space Invader" game created using Python's curses library. The game allows players to control a spaceship that can shoot bullets at descending alien spaceships. The objective is to eliminate as many enemies as possible without letting them reach the bottom of the screen.

Requirements
● Python 3.x
● curses library and random library

How to Play
● Controls:
○ Left Arrow (←): Move the spaceship left
○ Right Arrow (→): Move the spaceship right
○ Space Bar: Shoot a bullet upward
○ Q: Quit the game

● Objective:
○ Shoot the alien spaceships (V characters) descending from the top before
they reach the bottom.
○ Every successful hit increases the score by 10 points.

Main Components
1. Game Setup Functions:
○ setup_screen(): Initializes the game screen and sets up basic configurations like hiding the cursor and enabling special keys.
○ end_game(): Ends the game by resetting the terminal settings.

2. Game Over Display:
○ show_game_over(scr, score): Clears the screen and displays the final score and a "Game Over" message after the player loses.

3. Main Game Loop:
○ game(scr): Contains the main game logic, handling player input, movement and collisions.

4. Game Logic:
○ Player movement is limited to left and right within the screen boundaries.
○ Bullets move upwards, and enemies move downwards.
○ Collisions between bullets and enemies remove both, incrementing the score.
○ If any enemy reaches the bottom, the game ends.

Code Execution
Run the code by executing the following in a terminal:
Copy code
- python space_invader.py
Ensure that the terminal supports the curses library for the best experience. Press 'q' to quit the game at any point.
