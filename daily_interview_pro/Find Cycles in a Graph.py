# Given an undirected graph, determine if a cycle exists in the graph.
# Here is a function signature:
class UniqueList:
    def __init__(self):
        self.obj = []

    def append(self, val):
        if val in self.obj:
            raise ValueError
        else:
            self.obj.append(val)


keys_visited = UniqueList()


def _iter(g):
    for key, value in graph.items():
        try:
            keys_visited.append(key)
        except ValueError:
            return True
        if isinstance(value, dict):
            _iter(value)
    return False


def find_cycle(graph):
    # Fill this in.
    return _iter(graph)


graph = {
    'a': {'a2': {}, 'a3': {}},
    'b': {'b2': {}},
    'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
