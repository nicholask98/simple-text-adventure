import main

def determine_door_options():
    # FIXME: determine which directions the player has the option to go based on the grid located in main.py
    # ie. going up increases the player_pos value by 4 etc.

    if main.grid[main.player_pos]: # FIXME: This won't work because the grid is 2D
        pass
def prompt():
    return input('Which direction would you like to go?')