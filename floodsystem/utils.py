# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""
import math


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)


def dist(p1, p2):
    """
    Calculates the euclidean distance between two cartesian points given as tuples

    :param p1: Point 1 as a tuple
    :param p2: Point 2 as a tuple
    :return: Distance between points 1 and 2
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)