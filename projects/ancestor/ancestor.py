
from itertools import chain
def earliest_ancestor(ancestors, starting_node):
    child_to_parents = create_adjacency_list(ancestors)
    ancestor_path = get_ancestor_path(child_to_parents, [starting_node])
    if [starting_node] == ancestor_path:
        return -1
    else:
        return ancestor_path[-1]


def get_ancestor_path(graph, path):
    node = path[-1]
    if node not in graph:
        return path
    
    longest_path = None
    for parent in graph[node]:
        new_path = path + [parent]
        if longest_path is None:
            longest_path = get_ancestor_path(graph, new_path)
        else:
            test_path = get_ancestor_path(graph, new_path)
            if len(test_path) > len(longest_path):
                longest_path = test_path

        
    return longest_path



def create_adjacency_list(ancestor_pairs):
    family_tree = {}
    for parent, child in ancestor_pairs:
        if child in family_tree:
            family_tree[child].append(parent)
        else:
            family_tree[child] = [parent]

    return family_tree




if __name__=="__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 3))