import rooms
import movement

grid = [
        [8,  9, 10, 11],
        [4,  5,  6,  7],
        [0,  1,  2,  3],
    ]

visited_rooms = []
player_pos = grid[2][0]

def main():
    not_done = True
    while not_done: # not looping for testing purposes
        if player_pos not in visited_rooms:
            not_done = rooms.room(player_pos)
            visited_rooms.append(player_pos)
        else:
            print('You have already visited this room. Nothing more to see.')
            not_done = rooms.visited_room(player_pos)



if __name__ == '__main__':
    main()