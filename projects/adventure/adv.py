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


def has_unopened_door(player):
    id = player.current_room.id
    return None in player.map[id].values()


player.map_room()
visited_rooms = set([player.current_room.id])

while len(visited_rooms) < len(room_graph):
    while has_unopened_door(player):
        room = player.current_room
        exits = player.map[room.id]
        possible_exits = [i[0] for i in exits.items() if i[1] is None]
        x = random.choice(possible_exits)
        player.travel(x)
        if player.current_room.id in visited_rooms:
            player.map_room(x,room.id)
            player.travel(inv[x])
            continue
        traversal_path.append(x)
        visited_rooms.add(player.current_room.id)
        player.map_room(x, room.id)
        break

    return_path = player.BFS()
    if return_path:
        traversal_path.extend(return_path)
        for d in return_path:
            player.travel(d)



print(player.map)






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
