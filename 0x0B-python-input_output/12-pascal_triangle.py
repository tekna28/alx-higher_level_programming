#!/usr/bin/python3
"""Defines function that returns a list of lists of integers representing
Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's"""
    my_list = []
    for i in range(n):
        my_list.append([])
        for j in range(i+1):
            try:
                if j - 1 == -1:
                    my_list[i].append(1)
                else:
                    my_list[i].append(my_list[i-1][j-1] + my_list[i-1][j])
            except IndexError:
                my_list[i].append(1)
    return (my_list)
