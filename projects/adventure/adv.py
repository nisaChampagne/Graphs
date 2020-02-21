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

print(CYAN + 'START')

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/another_test.txt"
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
    stack = Stack()
    stack.push(world.starting_room)
    visited = set()
    while stack.size() > 0 :
        room = stack.pop()
        print(LIGHTGREEN + f'2~~~~ROOM: {room}')
        room_id = room.id
        print(LIGHTCYAN + f'3~~~~ROOM ID: {room_id}')

        if room_id not in map_graph.vertices:
            map_graph.add_vertex(room_id)

        exits = room.get_exits()
        print(LIGHTMAGENTA + f'4~~~~ROOM EXITS: {exits}')
        for direction in exits:
            adjacent_room = room.get_room_in_direction(direction)
            print(LIGHTRED + f'5~~~~ADJACENT ROOM: {adjacent_room}')
            adjacent_room_id = adjacent_room.id
            print(LIGHTYELLOW + f'6~~~~ADJACENT ROOM ID: {adjacent_room_id}')

            # if adjacent room not on map graph
            if adjacent_room_id not in map_graph.vertices:
                map_graph.add_vertex(adjacent_room_id)

            map_graph.add_edge(room_id, adjacent_room_id, direction)

            if adjacent_room_id not in visited:
                stack.push(adjacent_room)
        visited.add(room_id)



#2) keep track of rooms with directions
def find_next(room_id, visited, graph = map_graph):
    pass

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
