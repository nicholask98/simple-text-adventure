import movement



def room(room_num):
    options = movement.determine_door_options()
    if room_num == 0:
        print('You wake up in a room. There is a door in front of you and one to the right.')
        # Options holds a list that contains all the door option letters available
        direction = str(input("Enter the direction you'd like to go:{}".format(str(options)))).lower()
        movement.move(direction)
    elif room_num == 1:
        pass
    elif room_num == 2:
        pass
    elif room_num == 3:
        pass
    elif room_num == 4:
        pass
    elif room_num == 5:
        pass
    elif room_num == 6:
        pass
    elif room_num == 7:
        pass
    elif room_num == 8:
        pass
    elif room_num == 9:
        pass
    elif room_num == 10:
        pass
    elif room_num == 11:
        pass
    elif room_num == 13:
        print('You escaped!')
        return False
    return True

def visited_room(room_num):
    options = movement.determine_door_options()
    direction = str(input("Enter the direction you'd like to go:{}".format(str(options)))).lower()
    movement.move(direction)
    # FIXME: When I run main, I only get two cycles through the game loop.
    # I think it has something to do with the 2nd time through the loop
    # being treated as you're revisiting a room instead of encountering
    # a new one. More details on movement.py
    return False