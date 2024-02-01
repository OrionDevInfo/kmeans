# Author: ORION

from random import randint
from doctest import testmod

# Initial data
g1 = [[5, 3], [5, 6], [5, 0], [4, 3], [0, 3], [2, 4], [5, 5], [6, 2], [2, 2], [4, 4]]
g1 = [[5, 3], [5, 6], [5, 0], [4, 3], [0, 3], [2, 4], [5, 5], [6, 2], [2, 2], [4, 4]]
g2 = [
    [9, 10],
    [10, 10],
    [11, 11],
    [11, 10],
    [8, 12],
    [13, 10],
    [10, 9],
    [8, 8],
    [12, 10],
    [9, 9],
]
g3 = [
    [10, 1],
    [9, 3],
    [8, 4],
    [7, 2],
    [11, 1],
    [9, 2],
    [12, 3],
    [10, 1],
    [9, 4],
    [10, 3],
]
g4 = [
    [4, 17],
    [5, 14],
    [4, 15],
    [5, 13],
    [4, 13],
    [7, 13],
    [6, 12],
    [6, 14],
    [4, 12],
    [4, 17],
]
g = []
for g_i in [g1, g2, g3, g4]:
    for p in g_i:
        g.append(p)


def distance(p1, p2):
    """
    >>> distance([0, 0], [3, 4])
    5.0
    """
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def init_centroids(n):
    """
    >>> len(init_centroids(4)) == 4 and all(0<=x[0]<=20 and 0<=x[1]<=20 for x in init_centroids(4))
    True
    """
    return [[randint(0, 20), randint(0, 20)] for i in range(n)]


def closest(c, p):
    """
    >>> closest([[0,3],[3,3],[0,2],[4,4]], [0,1])
    2
    """
    return min(range(len(c)), key=lambda i: distance(c[i], p))


def allocation(c, pts):
    """
    >>> allocation([[0,3],[3,3],[0,2],[4,4]], [[0,1],[1,1],[2,1],[3,1]])
    [[], [[2, 1], [3, 1]], [[0, 1], [1, 1]], []]
    """
    return [[p for p in pts if closest(c, p) == i] for i in range(len(c))]


def barycenter(pts):
    """
    >>> barycenter([[0,1],[1,1],[2,1],[3,1]])
    [1.5, 1.0]
    """
    return (
        [sum(p[i] for p in pts) / len(pts) for i in range(len(pts[0]))]
        if len(pts) > 0
        else [0, 0]
    )


def calibration(c, pts):
    """
    >>> calibration([[0,3],[3,3],[0,2],[4,4]], [[0,1],[1,1],[2,1],[3,1]])
    [[0, 0], [2.5, 1.0], [0.5, 1.0], [0, 0]]
    """
    return [barycenter(group) for group in allocation(c, pts)]


def k_means(k, pts):
    return allocation(init_centroids(k), pts)


# Example
# print(k_means(4, g))
# [
#     [[4, 17], [4, 17]],
#     [
#         [5, 3],
#         [5, 6],
#         [5, 0],
#         [4, 3],
#         [0, 3],
#         [2, 4],
#         [5, 5],
#         [6, 2],
#         [2, 2],
#         [4, 4],
#         [10, 1],
#         [9, 3],
#         [8, 4],
#         [7, 2],
#         [11, 1],
#         [9, 2],
#         [12, 3],
#         [10, 1],
#         [9, 4],
#         [10, 3],
#     ],
#     [
#         [9, 10],
#         [8, 12],
#         [8, 8],
#         [9, 9],
#         [5, 14],
#         [4, 15],
#         [5, 13],
#         [4, 13],
#         [7, 13],
#         [6, 12],
#         [6, 14],
#         [4, 12],
#     ],
#     [[10, 10], [11, 11], [11, 10], [13, 10], [10, 9], [12, 10]],
# ]


# Bonus
import matplotlib.pyplot as plt


def kmeans(k, pts, n=6):
    c = init_centroids(k)
    plt.scatter([p[0] for p in pts], [p[1] for p in pts], c="black")
    print(c)
    colors = ["b", "g", "r", "c", "m", "y"]
    for i in range(n):
        color = colors[i % len(colors)]
        c = calibration(c, pts)
        plt.plot([p[0] for p in c], [p[1] for p in c], "{}+".format(color))
    plt.show()
    return c


# Example
print(kmeans(4, g))
# [[4, 2], [1, 0], [12, 15], [5, 16]]
# [[9.5, 2.4], [3.8, 3.2], [10.1, 9.9], [4.9, 14.0]]

testmod(verbose=False)
