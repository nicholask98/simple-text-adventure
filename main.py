import rooms
import movement

grid = [
        [8,  9,  10, 11],
        [4,  5,  6,  7],
        [0,  1,  2,  3],
    ]

visited_rooms = []
player_pos = 0

def main():

    # while True: # not looping for testing purposes
    if player_pos not in visited_rooms:
        rooms.room(player_pos)
    else:
        print('You have already visited this room. Nothing more to see.')
    




if __name__ == '__main__':
    main()