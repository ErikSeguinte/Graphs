from collections import deque
from room import Room
from player import Player
from world import World
from pathlib import Path

import random
from collections import deque
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# path = Path("projects/adventure/" + map_file)
path = map_file
# Loads the map into a dictionary
room_graph=literal_eval(open(path, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player:Player = Player(world.starting_room)
player.path_taken = deque()

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited_rooms = set()

inv = {
    'n':'s',
    's':'n',
    'w':'e',
    'e':'w',
}
graph = {}

def traverse_path(player, path_taken = None ):
    if path_taken is not None:
        # print(f"moving {path_taken}")
        player.travel(path_taken)
    room = player.current_room
    global visited_rooms
    global inv
    if room.id in visited_rooms:
        player.travel(inv[path_taken])
        return
    
    visited_rooms.add(room.id)
    if path_taken is not None:
        player.path_taken.append(path_taken)
    exits = room.get_exits()
    # print(f"room: {room.id}, exits: {exits}")

    for x in exits:
        if x != inv.get(path_taken):
            traverse_path(player, x)

    if path_taken is not None:
        # print(f"reversing: {inv[path_taken]}")
        if len(visited_rooms) == len(room_graph):
            return
        player.path_taken.append(inv[path_taken])
        player.travel(inv[path_taken])


traverse_path(player)
print(player.path_taken)

traversal_path = player.path_taken
        





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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
