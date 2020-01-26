from pprint import pprint
from typing import List, Tuple, NamedTuple, Dict, TypeVar
from math import copysign

# ###Typing### #
Node = TypeVar('Node')

class Edge(NamedTuple):
    src: Node
    dest: Node
    min_cap: int
    flow: int
    capacity: int
    
Graph = List[Edge]


# ###Algorithm### #
def get_surrounding(graph: Graph, center: Node) -> Dict[Node, int]:
    surrounding = {}
    for e in graph:
        if e.src == center:
            surrounding[e.dest] = e.capacity - e.flow
        if e.dest == center:
            surrounding[e.src] = -e.flow

    return surrounding

def test_paths(surrounding: Dict[Node, int], flow: int, marked: List[Node]) -> Dict[Node, int]:
    valid_paths = {}
    for n in surrounding:
        if (n not in marked) and (surrounding[n] != 0):
            f = min(abs(surrounding[n]), flow)
            f = copysign(f, surrounding[n])
            valid_paths[n] = f
    
    return valid_paths

def list_paths(graph: Graph, source: Node, sink: Node, flow: int, marked: List[Node]):
    surrounding = get_surrounding(graph, source)
    valid_paths = test_paths(surrounding, flow, marked)
    
    if sink in valid_paths:
        return
    
    marked.extend(valid_paths.keys())
    
    for p in valid_paths:
        marked = list_paths(graph, p, sink, abs(valid_paths[p]), marked)

def max_flow(edges, source: Node, sink: Node):
    graph = [Graph(*e) for e in edges]
    marked = [source]

    finished = False
    while not finished:
        marked = list_paths(graph, source, sink, None, marked)

    return graph


# ###Tests### #
if __name__ == "__main__":
    import dataset

    edges = [(1, 2, 0, 0, 24),
             (1, 4, 0, 0, 20),
             (3, 1, 0, 0, 6),
             (1, 3, 0, 0, 3),
             (3, 1, 0, 0, 5),
             (4, 3, 0, 0, 12)]

    graph = max_flow(edges, 1)
    pprint(graph)
