"""
The greedy solver class contains the different greedy solvers for the knapsack problem
"""
from collections import namedtuple
import pandas as pd
from operator import attrgetter, itemgetter
import time


class Greedy_solvers(object):
    """
    Object which contains different optimsation solver algorithms
    """

    def __init__(self):
        # self.items = items
        # self.capacity = capacity
        self.type = "greedy"

    def iter_named_tuples(self, df):
        """
        Helper function to create named tuples from a dataframe

        Returns a named tuple with the column names of the dataframe
        """
        Row = namedtuple('Item', df.columns)
        for row in df.itertuples():
            yield Row(*row[1:])

    def sort_by_value_per_weight(self, items):
        """
        Calculates the value per unit of weight for each item

        Returns ordered list of tuples by value/weight ratio
        """
        # convert tuples into dataframe to vectorise calculations
        df = pd.DataFrame(items, columns=['index', 'value', 'weight'])
        # calculate value/weight ratio for each item
        df["v_w_ratio"] = df.value / df.weight
        # sort dataframe by value/weight ratio then by weight to get the
        # lightest items first if there are equal weights
        df.sort_values(["v_w_ratio", "weight"],
                       ascending=[False, True], inplace=True)
        # convert table back into list of named tuples
        lst_items = list(self.iter_named_tuples(df))
        # update items
        return lst_items

    def solve_by_v_w_ratio(self, items, capacity):
        """
        Greedy solver by value per weight ratio

        Returns the solution in in a dictionary with the
        required items of the course
        """
        # sort the items by value/weight ratio
        items = self.sort_by_value_per_weight(items)

        # run the greedy solver
        value = 0
        weight = 0
        taken = [0]*len(items)

        # time algorithm
        start_t = time.time()
        for item in items:
            if weight + item.weight <= capacity:
                taken[item.index] = 1
                value += item.value
                weight += item.weight

        # calculate time required in hours
        duration = (time.time() - start_t)/3600.0
        # prepare the solution in the specified output format
        dct_output_data = {"obj": int(value),
                           "opt": str(0),
                           "decision": ' '.join(map(str, taken)),
                           "solver": "ratio",
                           "time_h": duration,
                           "weight": weight}
        return dct_output_data

    def sort_by_weight(self, items):
        """
        Sorts the items by weight.

        Returns ordered list of tuples by weight
        """
        return sorted(items, key=attrgetter("weight"), reverse=False)

    def solve_by_weight(self, items, capacity):
        """
        Greedy solver by weight of the items

        Returns the solution in in a dictionary with the
        required items of the course
        """
        # sort the items by wieght
        items = self.sort_by_weight(items)

        # run the greedy solver
        value = 0
        weight = 0
        taken = [0]*len(items)
        
        # time algorithm
        start_t = time.time()
        for item in items:
            if weight + item.weight <= capacity:
                taken[item.index] = 1
                value += item.value
                weight += item.weight

        # calculate time required in hours
        duration = (time.time() - start_t)/3600.0
        # prepare the solution in the specified output format
        dct_output_data = {"obj": int(value),
                           "opt": str(0),
                           "decision": ' '.join(map(str, taken)),
                           "solver": "weight",
                           "time_h": duration}
        return dct_output_data

    def solve(self, items, capacity):
        """
        Solves the optimisation with all available solvers and keeps
        the best value.

        Returns the best output for the data set in the required format
        """
        # create list of greedy solvers
        lst_greedy_solvers = [
            self.solve_by_weight,
            self.solve_by_v_w_ratio]
        # iterate through each solver
        # keep the results of each solver in a list of dictionaries so
        # that it can be sorted
        results = []
        for solver in lst_greedy_solvers:
            results.append(solver(items, capacity))
        # sort by best objective value
        sorted_results = sorted(results, key=itemgetter("obj"), reverse=True)
        # return the best result to the overall list
        return sorted_results[0]
