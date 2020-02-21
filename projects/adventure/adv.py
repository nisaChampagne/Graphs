from room import Room
from player import Player
from world import World
from util import Graph, Stack, Queue

import random
from ast import literal_eval

PURPLE = "\033[95m"
CYAN ="\033[96m"
DARKCYAN = "\033[36m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"
LIGHTRED     = "\033[91m"
LIGHTGREEN   = "\033[92m"
LIGHTYELLOW  = "\033[93m"
LIGHTBLUE    = "\033[94m"
LIGHTMAGENTA = "\033[95m"
LIGHTCYAN    = "\033[96m"
BACKGROUNDRED          = "\033[41m"
BACKGROUNDGREEN        = "\033[42m"
BACKGROUNDYELLOW       = "\033[43m"
BACKGROUNDBLUE         = "\033[44m"
BACKGROUNDMAGENTA      = "\033[45m"
BACKGROUNDCYAN         = "\033[46m"
BACKGROUNDLIGHTGRAY    = "\033[47m"
BACKGROUNDDARKGRAY     = "\033[100m"
BACKGROUNDLIGHTRED     = "\033[101m"
BACKGROUNDLIGHTGREEN   = "\033[102m"
BACKGROUNDLIGHTYELLOW  = "\033[103m"
BACKGROUNDLIGHTBLUE    = "\033[104m"
BACKGROUNDLIGHTMAGENTA = "\033[105m"
BACKGROUNDLIGHTCYAN    = "\033[106m"

print(CYAN + 'START')

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt" 
#  <---- this one is what sprint is on

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print(LIGHTBLUE + f'1~~~~STARTING ROOM: {world.starting_room}')


map_graph = Graph()

#1) populate graph by traversing through all the rooms
def populate_map():
    #create empty stack
    stack = Stack()
    # push starting room to stack
    stack.push(world.starting_room)
    #create empty list for visited rooms
    visited = set()
    # while stack size is not 0
    while stack.size() > 0 :
        #pop out room from stack
        room = stack.pop()
        print(LIGHTGREEN + f'2~~~~ROOM: {room}')
        #variable name given to value
        room_id = room.id
        print(LIGHTCYAN + f'3~~~~ROOM ID: {room_id}')

        # if room_id not in the map
        if room_id not in map_graph.vertices:
            # add it
            map_graph.add_vertex(room_id)

        #exits hold directions, room.get_exits() comes from room model
        exits = room.get_exits()
        print(LIGHTMAGENTA + f'4~~~~ROOM EXITS: {exits}')

        #for each cardinal direction in exits:
        for direction in exits:
            #grab the adjacent room
            adjacent_room = room.get_room_in_direction(direction)
            print(BLUE + F"DIRECTION: {direction}")
            print(LIGHTRED + f'5~~~~ADJACENT ROOM: {adjacent_room}')
            #variable to value for easier access
            adjacent_room_id = adjacent_room.id
            print(LIGHTYELLOW + f'6~~~~ADJACENT ROOM ID: {adjacent_room_id}')

            # if adjacent room not on map graph
            if adjacent_room_id not in map_graph.vertices:
                #add it to map
                map_graph.add_vertex(adjacent_room_id)

            #add edge to map via params
            map_graph.add_edge(room_id, adjacent_room_id, direction)

            # if id not in visited
            if adjacent_room_id not in visited:
                # add the adjacent room to stack 
                stack.push(adjacent_room)
        # add room id to visited set
        visited.add(room_id)



#2) keep track of rooms with directions , dead ends or not
def keep_track_of_rooms(room_id, visited, graph = map_graph):
    '''
    - will take in a room id and set of visited room ids
    - will return a set of moves that the player can take to get to closest space that hasnt been visited

    '''
    #create empty queue
    room_queue = Queue()
    # Add a list with room_id to the queue
    room_queue.enqueue([[room_id], []])
    #create an empty set that will hold rooms with moves
    rooms_with_moves = set()
    # add the current room_id to the set
    rooms_with_moves.add(room_id)
    print(BACKGROUNDBLUE + F"7~~~~{rooms_with_moves}")

    # while queue isnt empty
    while room_queue.size() > 0 :
        #grab off queue
        rooms, moves = room_queue.dequeue()
        #grab last room id from 
        last_room_id = rooms[-1]
        print(BACKGROUNDGREEN + F"8~~~~rooms: {rooms}, moves: {moves}")
        print(BACKGROUNDCYAN + F"9~~~~LAST ROOM ID: {last_room_id}")

        #grab neighbors via method from graph in util.py
        neighbors = graph.get_neighbors(last_room_id)
        print(BACKGROUNDLIGHTMAGENTA + F"10~~~~~NEIGHBORS: {neighbors}")

        #get copy of the directions which are the keys in the key:value pair
        neighbors_keys = list(neighbors.keys())
        print(BLUE + F"11~~~~~~neighbors_keys: {neighbors_keys}")

        # if dead end reached, return set of directions
        if len(neighbors_keys) == 1 and neighbors[neighbors_keys[0]] not in visited:
            #make copy of moves + the first key in neighbors_key
            dead_end = list(moves) + [neighbors_keys[0]]
            print(CYAN + F"12~~~~~~DEAD END: {dead_end}")
            return dead_end
        
        else:
            # keep going through
            for direction in neighbors:
                # variable pointing to next room hense the name
                next_room = neighbors[direction]
                # rooms + next room = new_room
                new_room = rooms + [next_room]
                # new direction
                new_moves = moves + [direction]
                print(BACKGROUNDRED + F"13~~~~~~\nNEXT ROOM: {next_room}\n ROOMS: {rooms} \n NEW ROOM: {new_room} \n NEW MOVES: {new_moves}")
                # if next_room not in rooms with moves
                if next_room not in rooms_with_moves:
                    # add it to queue
                    room_queue.enqueue([new_room, new_moves])
                    # add next room to rooms with moves
                    rooms_with_moves.add(next_room)
                    print(BACKGROUNDLIGHTRED + f"14~~~~ \nROOM WITH MOVES: {rooms_with_moves}")
                if next_room not in visited:
                    return new_moves


#3) call populate graph function (populate_graph())
populate_map()

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#4) when length of visited is less than number of rooms:
        #- find a path
        #- traverse the returned list of moves
        #-update current room

'''

FROM READ ME:
You may find the commands `player.current_room.id`, 
`player.current_room.get_exits()`
 and `player.travel(direction)` useful.


 -relationship in current room provided tuple --> coordinates

I will start out  with the smallest map to make sure my traversal works

im thinking of having a util file with queue and stack available

maybe a traversal BFS as we don't have anything we are actively seeking out

possible game plan:
    1) populate graph by traversing through all the rooms

    2) keep track of rooms with directions

    3) call populate graph function (populate_graph())

    4) when length of visited is less than number of rooms:
        - find a path
        - traverse the returned list of moves
        -update current room
'''

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(PURPLE + f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(PURPLE + f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
