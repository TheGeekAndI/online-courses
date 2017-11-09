#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from greedy_solvers import Greedy_solvers
from dynamic_prog_solver import Dynamic_solvers
from least_discrepancy_solver import Lds_solvers
from operator import itemgetter
import pprint


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

    # ### Solve the problem with all available solvers ###

    # intialise a list where the best result from each solver type is stored
    results = []

    # ### solve the knapsack problem with greedy solvers ###
    # create a greedy solver object
    gs = Greedy_solvers()
    # solve with all greedy solvers
    results.append(gs.solve(items, capacity))

    # ### solve the knapsack problem with dynamic programmins solvers ###
    # create a dp solver object
    dps = Dynamic_solvers()
    # solve will all available dp solvers if enough memory is available
    dps_result = dps.solve(items, capacity)
    # only append results if it is not none so that the sorting step works
    # correctly
    if dps_result:
        results.append(dps_result)

    # ### solve the knapsack problem with least discrepancy search
    lds = Lds_solvers()
    # solve with all available solvers in the group:
    # currently best_estimate relaxation and non-integrality relaxation
    lds_result = lds.solve(items, capacity)
    # only append results if it is not none so that the sorting step works
    # correctly
    if lds_result:
        results.append(lds_result)

    pprint.pprint(results)
    # sort the results by the objective function and pick the best one
    sorted_results = sorted(results, key=itemgetter("obj"), reverse=True)
    # create the required output by the submitter
    output_data = str(sorted_results[0]["obj"]) + " "\
        + sorted_results[0]["opt"] + '\n'
    output_data += sorted_results[0]["decision"] + '\n'

    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print("This test requires an input file. "
              "Please select one from the data directory. "
              "(i.e. python solver.py ./data/ks_4_0)")
