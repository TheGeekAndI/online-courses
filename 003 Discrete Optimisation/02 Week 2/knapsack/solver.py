#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from v_w_ratio_solver import V_w_solver
# import pprint

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    ### solve the knapsack problem with the value/weight ratio solver ###

    # create a value weight ratio solver object
    vws = V_w_solver(items, capacity)
    
    # reorder the items by value weight ratio
    vws.items = vws.value_per_weight()
    
    # solve by greedy on value weight ratio
    return vws.solve_by_v_w_ratio()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

