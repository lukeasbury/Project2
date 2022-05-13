from game import Game

"""
Original Project Idea: https://www.youtube.com/watch?v=delJJ9zHXio

Features Added: GUI Interface, Main Menu, Website redirect, Program Screen
"""
g = Game()

"""
Used to start the game and display menu screen
"""

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    