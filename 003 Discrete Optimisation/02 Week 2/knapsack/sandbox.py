# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 08:31:00 2017

@author: parenti daniele
"""
from collections import namedtuple
from operator import attrgetter, itemgetter
import pprint
import numpy as np
import pandas as pd
import psutil

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
    
#%%

def populate_dynamic_table(items, capacity):
    # convert the tupes into a table so the information can be easily retrieved
    df_items = pd.DataFrame(items, columns=['index', 'value', 'weight'])
    df_items.set_index("index", inplace=True)
    values = df_items["value"]
    weights = df_items["weight"]
    # initalise a numpy array of zeros with rows = capacity and colums = items +1
    space = pd.DataFrame(np.zeros((capacity+1, len(items)+1), dtype=np.int))
    
    # iterate over each column from 1 and each row
    for i in range(1, len(space.columns)):
        for j in range(0, len(space)):
        
#%%
print((psutil.virtual_memory().available))
print((psutil.virtual_memory().available)*.9)

required_mem = (len(items)+1)*(capacity+1)*8

if psutil.virtual_memory().available < required_mem:
    print("good")
#%%

dps_result = None

if dps_result:
    print("Append")
#else:
#    print("Dont")
#%%

import itertools
    # find all permutations of decision vector and store in a list
decision_options = []
[decision_options.append(seq) for seq in itertools.product([0,1], repeat=len(items))]
lst_decisions_options = [list(elem) for elem in decision_options]




    # for each element in the list
        # iterate through each element of the vector:
            # sum the weight of the vector
            # if the weight of the vector exceeds capacity drop the branch
            # else calculate the value

            # if the value is less than the current best value drop the branch
            # otherwise update the max value