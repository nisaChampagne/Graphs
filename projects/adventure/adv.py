from room import Room
from player import Player
from world import World
from util import Graph, Stack, Queue

import random
from ast import literal_eval

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
print(world.starting_room, 'STARTING ROOM')


map_graph = Graph()
print(map_graph, 'map')

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

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
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
