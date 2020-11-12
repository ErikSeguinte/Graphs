"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id) -> set:
        """
        Get all neighbors (edges) of a vertex.
        """
        v:set = self.vertices[vertex_id]

        return v.difference(self.visited)


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        self.visited = {starting_vertex}
        q.enqueue(starting_vertex)


        while len(q) != 0:
            node = q.dequeue()
            print(node)
            to_visit:set = self.get_neighbors(node)
            q.multi_enqueue(to_visit)
            self.visited = self.visited.union(to_visit)

        self.visited = set()
        print()



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        self.visited = {starting_vertex}
        q.push(starting_vertex)


        while len(q) != 0:
            node = q.pop()
            print(node)
            to_visit:set = self.get_neighbors(node)
            q.multi_push(to_visit)
            self.visited = self.visited.union(to_visit)

        self.visited = set()
        print()


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        self.dft_recurse(starting_vertex)
        self.visited = set()
        print()
        
    def dft_recurse(self, v):
        if v in self.visited:
            return None
        
        print(v)
        self.visited.add(v)

        neighbors = self.get_neighbors(v)

        for n in neighbors:
            self.dft_recurse(n)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print("# BFS")
        q = Queue()
        self.visited = {1}
        q.enqueue([starting_vertex])


        while len(q) != 0:
            path = q.dequeue()
            if path[-1] == destination_vertex:
                return path

            to_visit:set = self.get_neighbors(path[-1])
            
            new_q = [path + [n] for n in to_visit]

            q.multi_enqueue(new_q)
            self.visited = self.visited.union(to_visit)

        self.visited = set()
        print()


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print("# DFS")
        q = Stack()
        self.visited = {1}
        q.push([starting_vertex])


        while len(q) != 0:
            path = q.pop()
            if path[-1] == destination_vertex:
                self.visited = set()
                return path

            to_visit:set = self.get_neighbors(path[-1])
            
            new_q = [path + [n] for n in to_visit]

            q.multi_push(new_q)
            self.visited = self.visited.union(to_visit)

        print()

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("# dfs_r")
        result = self.dfs_recurse([starting_vertex], destination_vertex)
        self.visited = set()
        return result
        
    def dfs_recurse(self, p, d):
        v = p[-1]
        if v in self.visited:
            return None
        
        if v == d:
            return p
        
        self.visited.add(v)

        neighbors = self.get_neighbors(v)

        for n in neighbors:
            result = self.dfs_recurse(p + [n], d)
            if result:
                return result


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
