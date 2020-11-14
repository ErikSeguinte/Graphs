from collections import deque
inv = {
    'n':'s',
    's':'n',
    'w':'e',
    'e':'w',
}
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.path_taken = []
        self.map = {}

    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if show_rooms:
                next_room.print_room_description(self)
        else:
            print(f"room: {self.current_room.id}, trying {direction}")
            print("You cannot move in that direction.")
            # breakpoint()

    def map_room(self, direction_taken = None, prev = None):
        id = self.current_room.id
        if id not in self.map:
            exits = self.current_room.get_exits()
            if len(exits) > 0:
                self.map[id] = {}

                for x in exits:
                    self.map[id][x] = None
        if prev is not None:
            self.map[id][inv[direction_taken]] = prev
            self.map[prev][direction_taken] = id

    def BFS(self):
        q = deque([[(None, self.current_room.id)]])
        visited = set()

        while q:
            path = q.pop()
            room = path[-1][1]
            visited.add(room)
            exits = self.map[room]
            if None in exits.values():
                return [item[0] for item in path[1:]]
            else:
                for k, v in exits.items():
                    if v not in visited:
                        new_path = path + [(k, v)]
                        q.append(new_path)



