from pprint import pprint
from typing import List, Tuple, NamedTuple, Dict, TypeVar

# ###Typing### #
Node = TypeVar('Node')
Edges = List[Tuple[Node, Node, int]]


class Mark(NamedTuple):
    marked: Node
    weight: int
    marker: Node


# ###Algorithm### #
def get_successors(edges: Edges, s: Mark) -> Dict[Node, int]:
    successors = {}
    for e in edges:
        if e[0] == s.marked:
            successors[e[1]] = e[2]
        if e[1] == s.marked:
            successors[e[0]] = e[2]
    return successors


def merge_marks(marks: List[Mark], exclude_marks: List[Mark], successors: Dict[Node, int], start: Mark) -> List[Mark]:
    offset = start.weight
    s = start.marked
    excluded = [m.marked for m in exclude_marks]

    for i in range(len(marks)):
        mark = marks[i]
        if mark.marked in successors:
            weight = successors[mark.marked] + offset
            del successors[mark.marked]
            if weight < mark.weight:
                marks[i] = Mark(mark.marked, weight, s)

    for k in successors:
        if k not in excluded:
            weight = successors[k] + offset
            marks.append(Mark(k, weight, s))

    return marks


def dijkstra(edges, s):
    final_marks = [Mark(s, 0, None)]
    temp_marks = []

    finished = False
    while not finished:
        successors = get_successors(edges, final_marks[-1])
        temp_marks = merge_marks(temp_marks, final_marks, successors, final_marks[-1])
        temp_marks.sort(key=lambda x: x.weight, reverse=True)

        if len(temp_marks) != 0:
            final_marks.append(temp_marks.pop())
        else:
            finished = True

    return final_marks


# https://www.hackerrank.com/challenges/dijkstrashortreach/problem
def shortestReach(n, edges, s):
    paths = dijkstra(edges, s)
    pprint(paths)
    paths = {m.marked: m.weight for m in paths}
    l = []
    for i in range(n):
        l.append(paths.get(i + 1, -1))
    del l[s - 1]

    return l


# ###Tests### #
if __name__ == "__main__":
    import dataset

    edges = [(1, 2, 24),
             (1, 4, 20),
             (3, 1, 3),
             (4, 3, 12)]

    shortest = dijkstra(dataset.edges, 1)
    pprint(shortest)
    shortest.sort(key=lambda x: x.marked)
    pprint(shortest)
