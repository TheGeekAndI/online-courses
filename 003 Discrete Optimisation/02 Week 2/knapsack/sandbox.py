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
import numpy as np
    # find all permutations of decision vector and store in a list
decision_options = []
[decision_options.append(seq) for seq in itertools.product([1,0], repeat=len(items))]
lst_decisions_options = [list(elem) for elem in decision_options]
    # for each element in the list
for decision_vector in lst_decisions_options:
    print(np.asarray(decision_vector).reshape(1,len(items)))
    # iterate through each element of the vector:
    for item, decision in enumerate(decision_vector):
        
        
        print(items[item].weight, items[item].value, decision)
        # iterate through each element of the vector:
            # sum the weight of the vector
            # if the weight of the vector exceeds capacity drop the branch
            # else calculate the value

            # if the value is less than the current best value drop the branch
            # otherwise update the max value
#%%
import itertools
import timeit

def myfunc(items):
    for decision_option in itertools.product([1,0], repeat=items):
        pass
    # unpack the tuple in to a list so it can be iterated
#        lst_decision_option = [(elem) for elem in decision_option]

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
i = 6
for i in range(2, 26):
    wrapped = wrapper(myfunc, i)
    print(i, timeit.timeit(wrapped, number = 1))

def mysubfunc(decision_option):
    lst_decision_option = [(elem) for elem in decision_option]
d = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
wrapped2 = wrapper(mysubfunc, d)
print(timeit.timeit(wrapped2))

#%%
import numpy
import itertools
import timeit

some_list = [1,0]
some_length = 25

#print(numpy.array(list(itertools.product(some_list, repeat=some_length))))

#print("---")
def myfunc(some_list, some_length):
    n = numpy.array(some_list)[numpy.rollaxis(
            numpy.indices((len(some_list),) * some_length), 0, some_length + 1)
            .reshape(-1, some_length)]
        
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(myfunc, some_list, some_length)
print(timeit.timeit(wrapped, number=1))

#%%


#%%
from operator import attrgetter
import itertools
import pprint
import pandas as pd
import time

best_value = 0 
best_decision = []

# sort items by value to truncate sooner
items = sorted(items, key=attrgetter("value"), reverse=True)
current_running_time = 0

do_start = time.time()
for decision_option in itertools.product([1,0], repeat=len(items)):
    current_running_time += time.time()- do_start
    print("current running time is {s} seconds".format(s=current_running_time))   
    # unpack the tuple in to a list so it can be iterated
    lst_decision_option = [(elem) for elem in decision_option]
    #
    filled_weight = 0
    filled_value = 0
    max_estimate = sum([item.value for item in items])
    
    for item, decision in enumerate(lst_decision_option):
        if decision > 0:
            filled_weight += items[item].weight
            filled_value += items[item].value
        else:
            max_estimate -= items[item].value

        if filled_weight > capacity or max_estimate < best_value:
            break
        
        if item+1 == len(items) and filled_weight <= capacity\
        and filled_value > best_value:
            best_value = filled_value
            best_decision = lst_decision_option
    
# the best decision contains the indexes of the sorted list.
# from the list index you can find the original index in the named tuple
# and rewrite the decision
df = pd.DataFrame({"decision": best_decision})
print(df)
lst=[]
for idx, row in df.iterrows():
    lst.append(items[idx].index)

df["o_index"] = lst
df.set_index("o_index", inplace=True)
df.sort_index(inplace=True)
print(df)

best_decision2 = df.decision.tolist()
print(best_decision2)
print(type(best_decision2))

dct_output_data = {"obj": int(best_value),
                           "opt": str(0),
                           "decision": ' '.join(map(str, best_decision2)),
                           "solver": "lds_best_est"}

pprint.pprint(dct_output_data)

#%%
def iter_named_tuples(df):
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

items2 = sort_by_value_per_weight(items)


value = 0
weight = 0
taken = [0]*len(items2)
for item in items2:
    if weight + item.weight <= capacity:
        taken[item.index] = 1
        value += item.value
        weight += item.weight
    else:
        remainder = capacity - weight
        fraction = remainder / weight
        value += item.value * fraction
        
    
print(weight)
print(value)

#%%
class Node:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string


class searchtree:

      def __init__(self): #constructor of class

          self.root = None


      def create(self,val):  #create binary search tree nodes

          if self.root == None:

             self.root = Node(val)

          else:

             current = self.root

             while 1:

                 if val < current.info:

                   if current.left:
                      current = current.left
                   else:
                      current.left = Node(val)
                      break;      

                 elif val > current.info:
                 
                    if current.right:
                       current = current.right
                    else:
                       current.right = Node(val)
                       break;      

                 else:
                    break 

      def bft(self): #Breadth-First Traversal

          self.root.level = 0 
          queue = [self.root]
          out = []
          current_level = self.root.level

          while len(queue) > 0:
                 
             current_node = queue.pop(0)
 
             if current_node.level > current_level:
                current_level += 1
                out.append("\n")

             out.append(str(current_node.info) + " ")

             if current_node.left:

                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  

             if current_node.right:

                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                      
                 
          print("".join(out))   


      def inorder(self,node):
            
           if node is not None:
              
              self.inorder(node.left)
              print(node.info)
              self.inorder(node.right)


      def preorder(self,node):
            
           if node is not None:
              
              print(node.info)
              self.preorder(node.left)
              self.preorder(node.right)


      def postorder(self,node):
            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              print(node.info)

                        
tree = searchtree()     
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
    tree.create(i)
print('Breadth-First Traversal')
tree.bft()
print('Inorder Traversal')
tree.inorder(tree.root) 
print('Preorder Traversal')
tree.preorder(tree.root) 
print('Postorder Traversal')
tree.postorder(tree.root)

#%%

class Node:
    """
    Each node is the currently defined state of the decision variable
    """
    
    