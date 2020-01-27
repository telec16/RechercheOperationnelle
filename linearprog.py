from pprint import pprint
from typing import List, Tuple


def get_pivot(data: List[List[float]]) -> Tuple[int, int]:
    """Return the coordinates of the best pivot point in the specified dataset

    :param data: the matrix to solve
    :return: the pivot point (x, y)
    """
    # Retrieve the minimum non-nul negative coefficient on the last line
    y = None
    c = 0
    for i in range(len(data[-1]) - 1):
        if data[-1][i] < c:
            y = i
            c = data[-1][i]

    # Retrieve the minimum (positive) second member/pivot ratio
    min_ratio = None
    x = None
    for i in range(len(data) - 1):
        if data[i][y] > 0:
            ratio = data[i][-1] / data[i][y]
            if min_ratio is None or min_ratio > ratio:
                min_ratio = ratio
                x = i

    return x, y


def subtract_lines(data: List[List[float]], x: int, y: int) -> None:
    """Subtract the given line to all the others,
    with a coefficient so that the given column become 0

    :param data: the matrix to solve
    :param x: the line to subtract to the others
    :param y: the column to nullify
    :return:
    """
    for i in range(len(data)):
        if i != x:
            coef = data[i][y] / data[x][y]
            for j in range(len(data[-1])):
                data[i][j] = data[i][j] - coef * data[x][j]


def divide_line(data: List[List[float]], x: int, y: int) -> None:
    """Divide each column of the given line
    by a coefficient so that the given pivot point become 1

    :param data: the matrix to solve
    :param x: the line to divide
    :param y: the column of the pivot point
    :return:
    """
    coef = data[x][y]
    for j in range(len(data[-1])):
        data[x][j] /= coef


if __name__ == "__main__":
    data1 = [[2, 4, 1, 2, 1, 0, 0, 0, 0, 45],
            [4, 10, 0, 0, 0, 1, 0, 0, 0, 70],
            [1, 0, 4, 5, 0, 0, 1, 0, 0, 40],
            [0, 0, 5, 10, 0, 0, 0, 1, 0, 70],
            [-.3, -.4, -.5, -.8, 0, 0, 0, 0, 1, 0]]
    data2 = [[-1, 4, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [5, 4, 3, 0, -1, 0, 1, 0, 0, 0, 4],
            [0, 1, 2, 1, 0, 0, 0, 1, 0, 0, 2],
            [1, -2, -1, 1, 1, 0, 0, 0, 1, 0, 3],
            [-1, -4, 2, 0, -10, 0, 0, 0, 0, 1, 0]]

    data = data1

    while not all([d >= 0 for d in data[-1]]):
        pivot = get_pivot(data)
        print(pivot)
        subtract_lines(data, *pivot)
        divide_line(data, *pivot)

        pprint(data, width=160)
