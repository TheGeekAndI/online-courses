"""
Least discrepancy optimiser
"""
import itertools
from operator import itemgetter
import time


class Lds_solvers(object):
    """
    Contains methods to solve an optimisation problem through a
    least discrepancy approach
    """

    def __init__(self):
        self.type = "LDS"

    def lds_best_estimate_solver(self, items, capacity):
        """
        Least discrepancy optimisation solver based on the items
        and capacity provided.

        Returns the solution in in a dictionary with the 
        required items of the course.
        """
        best_value = 0
        best_decision = []

        # time algorithm
        start_t = time.time()

        # create a possible permutation of the decision vector at a time
        for decision_option in itertools.product([1, 0], repeat=len(items)):
            # unpack the tuple in to a list so it can be iterated
            lst_decision_option = [(elem) for elem in decision_option]

            # best estimate relaxation
            best_estimate = sum([item.value for item in items])

            filled_weight = 0
            filled_value = 0
            
            # iterate over each item in the possible decision vector
            # so that the tree can be pruned as soon as the best estimate
            # is less than the best identified value
            for item, decision in enumerate(lst_decision_option):
                # if the item is selected update the values
                if decision > 0:
                    filled_weight += items[item].weight
                    filled_value += items[item].value
                else:
                    # update the best possible estimate for the remainder of
                    # the branch
                    best_estimate -= items[item].value

                if filled_weight > capacity or best_estimate < best_value:
                    break
                
                if item+1 == len(items) and filled_weight <= capacity\
                        and filled_value > best_value:
                            best_value = filled_value
                            best_decision = lst_decision_option
        
        # calculate time required in hours
        duration = (time.time() - start_t)/3600.0

        # prepare the solution in the specified output format
        dct_output_data = {"obj": int(best_value),
                           "opt": str(1),
                           "decision": ' '.join(map(str, best_decision)),
                           "solver": "lds_best_est",
                           "time_h": duration}
        return dct_output_data

    def lds_non_int_est_solver(self, items, capacity):
        """
        Least discrepancy optimisation solver based on the items
        and capacity provided with a non integrality relaxation.

        Returns the solution in in a dictionary with the
        required items of the course.
        """
        best_value = 0
        best_decision = []

        # time algorithm
        start_t = time.time()

        # create a possible permutation of the decision vector at a time
        for decision_option in itertools.product([1, 0], repeat=len(items)):
            # unpack the tuple in to a list so it can be iterated
            lst_decision_option = [(elem) for elem in decision_option]

            # best estimate relaxation
            best_estimate = sum([item.value for item in items])

            filled_weight = 0
            filled_value = 0
            
            # iterate over each item in the possible decision vector
            # so that the tree can be pruned as soon as the best estimate
            # is less than the best identified value
            for item, decision in enumerate(lst_decision_option):
                # if the item is selected update the values
                if decision > 0:
                    filled_weight += items[item].weight
                    filled_value += items[item].value
                else:
                    # update the best possible estimate for the remainder of
                    # the branch
                    best_estimate -= items[item].value

                if filled_weight > capacity or best_estimate < best_value:
                    break
                
                if item+1 == len(items) and filled_weight <= capacity\
                        and filled_value > best_value:
                            best_value = filled_value
                            best_decision = lst_decision_option
        
        # calculate time required in hours
        duration = (time.time() - start_t)/3600.0

        # prepare the solution in the specified output format
        dct_output_data = {"obj": int(best_value),
                           "opt": str(0),
                           "decision": ' '.join(map(str, best_decision)),
                           "solver": "lds_best_est",
                           "time_h": duration}
        return dct_output_data

    def solve(self, items, capacity):
        """
        Solves the optimisation with all available solvers and keeps
        the best value.

        Returns the best output for the data set in the required format
        """
        # create list of greedy solvers
        lst_lds_solvers = [
            self.lds_best_estimate_solver]
        # iterate through each solver
        # keep the results of each solver in a list of dictionaries so
        # that it can be sorted
        results = []
        for solver in lst_lds_solvers:
            results.append(solver(items, capacity))
        # sort by best objective value
        sorted_results = sorted(results, key=itemgetter("obj"), reverse=True)
        # return the best result to the overall list
        return sorted_results[0]
