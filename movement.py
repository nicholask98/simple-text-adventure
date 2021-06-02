import main

def determine_door_options():
    
    # initialize options list with all directions
    options = ['u', 'd', 'l', 'r']
   
    # remove options from options list if they aren't available
    # checks for left and right edge of grid
    if main.player_pos % 4 == 0:
        options.remove('l')
    if main.player_pos % 4 == 3:
        options.remove('r')
    # checks for top edge of grid, except for 9 (the exit)
    if main.player_pos == 8 or main.player_pos >= 10:
        options.remove('u')
    # aaaaand bottom edge
    if main.player_pos <= 3:
        options.remove('d')
    return options

def prompt():
    return input('Which direction would you like to go?')

def move(direction):
    if direction == 'r':
        main.player_pos += 1
    elif direction == 'l':
        main.player_pos -= 1
    elif direction == 'u':
        main.player_pos += 4
    elif direction == 'd':
        main.player_pos -= 4
    
    # FIXME: This value for main.player_pos is different from the one I print at the beginning of the game loop.
    # Does changing the value assigned to a variable not take effect immediately from outside it's original module?
    # That doesn't seem right, but I can't figure out why movement.move() doesn't change the main.player_pos int.
    print(main.player_pos)

    
    