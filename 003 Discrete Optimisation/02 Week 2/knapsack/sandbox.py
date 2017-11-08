# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 08:31:00 2017

@author: parenti daniele
"""
from collections import namedtuple
from operator import attrgetter, itemgetter
import pprint

#%%
def iter_named_tuples( df):
    """
    Helper function to create named tuples from a dataframe
    Returns a named tuple with the column names of the dataframe
    """
    Row = namedtuple('Item', df.columns)
    for row in df.itertuples():
        yield Row(*row[1:])

def sort_by_value_per_weight(items):
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
    lst_items = list(iter_named_tuples(df))
    # update items
    return lst_items

def solve_by_v_w_ratio(items):
        """
        Greedy solver by value per weight ratio
        Returns the solution in the specified format by the course
        """
        # sort the items by value/weight ratio
        items = sort_by_value_per_weight(items)

        # run the greedy solver
        value = 0
        weight = 0
        taken = [0]*len(items)

        for item in items:
            if weight + item.weight <= capacity:
                taken[item.index] = 1
                value += item.value
                weight += item.weight
                # print("current weight: {w}; current value: {v}".format(w=weight, v=value))

        # prepare the solution in the specified output format
        output_data = str(value) + ' ' + str(0) + '\n'
        output_data += ' '.join(map(str, taken))
        dct_output_data ={"obj": str(value),
                       "opt": str(0),
                       "decision": ' '.join(map(str, taken))}
        return dct_output_data

#%%
   
def sort_by_weight(items):
     """
     Sorts the items by weight
     Returns ordered list of tuples by weight
     """
     return sorted(items, key=attrgetter("weight"), reverse=False)

def solve_by_weight(items):
     """
     Greedy solver by weight of the items
     Returns the solution in the specified format by the course
     """
     # sort the items by wieght
     items = sort_by_weight(items)
    
     # run the greedy solver
     value = 0
     weight = 0
     taken = [0]*len(items)
    
     for item in items:
         if weight + item.weight <= capacity:
             taken[item.index] = 1
             value += item.value
             weight += item.weight
             # print("current weight: {w}; current value: {v}".format(w=weight, v=value))
    
     # prepare the solution in the specified output format
     output_data = str(value) + ' ' + str(0) + '\n'
     output_data += ' '.join(map(str, taken))
     dct_output_data ={"obj": str(value),
                       "opt": str(0),
                       "decision": ' '.join(map(str, taken))}
     return dct_output_data
 
    #%%
    
    # create a list of solver functions
lst_greedy_solvers = [
        solve_by_weight,
        solve_by_v_w_ratio]

results = []
for solver in lst_greedy_solvers:
    results.append(solver(items))

results
        

    
    # go through each list and solve the problem
       
        # store the objective value in a list
        
    # return the best solution
    
    