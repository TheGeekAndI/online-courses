"""
The dynamic programming solver class contains the dynamic programming solver
"""
import numpy as np
from operator import itemgetter
import psutil
import time


class Dynamic_solvers(object):
    """
    Object that contains the dynamic programming methods to solve
    optimisation problems
    """

    def __init__(self):
        self.type = "dynamic"

    def populate_dynamic_table(self, items, max_capacity):
        """
        Populates the dynamic programming search table

        Returns a numpy array with the optimal values
        """
        # initalise a numpy array of zeros with rows = capacity
        # and colums = items +1
        space = np.zeros((max_capacity+1, len(items)+1), dtype=np.int)
        # iterate over each column from 1 and each row
        for item in range(1, np.shape(space)[1]):
            for capacity in range(1, np.shape(space)[0]):
                # if the weight of the current item is less than the
                # capacity populate the value of the item
                if items[item-1].weight <= capacity:
                    space[capacity, item] = max(space[capacity, item-1],
                                                items[item-1].value + space[capacity - items[item-1].weight, item-1])            
                else:
                    space[capacity, item] = space[capacity, item-1]

        return space

    def traceback(self, items, space):
        """
        Creates the decision vector based on the dynamic programming
        search table

        Returns a tuple of the maximum objective value and the decision vector
        """
        #  go to the bottom right og the space
        value = space[-1, -1]
        taken = [0]*(len(items)+1)

        capacity = np.shape(space)[0]-1
        for item in range(len(items), -1, -1):
            # check if the value to the left is smaller than the current value
            if space[capacity, item-1] < space[capacity, item]:
                # set the decision variable to 1
                taken[item] = 1
                # reduce the used capacity by the taken item as we now look
                # for the next best item
                capacity -= items[item-1].weight

        # remove the first item from the taken vector as this when selecting
        # no items
        taken = taken[1:]

        return value, taken

    def solve_by_dp(self, items, capacity):
        """
        Solves the optimisation problem with a dynamic progamme

        Returns a dictionary of the required results
        """
        # time the algorithm
        start_t = time.time()
        space = self.populate_dynamic_table(items, capacity)
        value, taken = self.traceback(items, space)

        # calculate time required in hours
        duration = (time.time() - start_t)/3600.0

        dct_output_data = {"obj": int(value),
                           "opt": str(1),
                           "decision": ' '.join(map(str, taken)),
                           "solver": "dp",
                           "time_h": duration}
        return dct_output_data

    def solve(self, items, capacity):
        """
        Solves the optimisation with all available solvers and keeps the best
        value

        Returns the best output for the data set in the required format
        """
        # check if memory runs out, if yes dont do this solver
        # calculate memory required
        mem_required = (len(items)+1)*(capacity+1)*8.0

        # exit this solver if memory is likely to run out
        if (((len(items)+1) * (capacity+1)) > 10000000)\
                or ((psutil.virtual_memory().available)*0.9 < mem_required):
            return

        # create list of greedy solvers
        lst_dp_solvers = [
            self.solve_by_dp]
        # iterate through each solver
        # keep the results of each solver in a list of dictionaries so that
        # it can be sorted
        results = []
        for solver in lst_dp_solvers:
            results.append(solver(items, capacity))
        # sort by best objective value
        sorted_results = sorted(results, key=itemgetter("obj"), reverse=True)
        # return the best result to the overall list
        return sorted_results[0]
