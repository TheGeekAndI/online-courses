"""
The solver class contains the different solvers for the knapsack problem
"""
from collections import namedtuple
import pandas as pd
import pprint


class V_w_solver(object):
    """
    Object which contains different optimsation solver algorithms
    """

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def iter_named_tuples(self, df):
        """
        Helper function to create named tuples from a dataframe
        Returns a named tuple with the column names of the dataframe
        """
        Row = namedtuple('Item', df.columns)
        for row in df.itertuples():
            yield Row(*row[1:])

    def value_per_weight(self):
        """
        Calculates the value per unit of weight for each item
        Returns ordered list of tuples by value/weight ratio
        """
        # convert tuples into dataframe to vectorise calculations
        df = pd.DataFrame(self.items, columns=['index', 'value', 'weight'])
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

    def solve_by_v_w_ratio(self):
        """
        Greedy solver by value per weight ratio
        Returns the solution in the specified format by the course
        """
        # a greedy solver with value/weight ratio
        value = 0
        weight = 0
        taken = [0]*len(self.items)

        for item in self.items:
            if weight + item.weight <= self.capacity:
                taken[item.index] = 1
                value += item.value
                weight += item.weight
                # print("current weight: {w}; current value: {v}".format(w=weight, v=value))

        # prepare the solution in the specified output format
        output_data = str(value) + ' ' + str(0) + '\n'
        output_data += ' '.join(map(str, taken))
        return output_data
