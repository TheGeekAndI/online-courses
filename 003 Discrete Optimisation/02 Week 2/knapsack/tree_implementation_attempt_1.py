# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:41:37 2017

@author: parenti daniele
"""
import pprint
from collections import namedtuple


class Node:

      def __init__(self,item): #constructor of class

          self.index = item.index
          self.weight = item.weight
          self.value = item.value
          self.decision = None
          self.cumulative_weight = None
          self.best_estimate = None
          self.left = None  #left leaf
          self.right = None #right leaf

      def __str__(self):

          return str(self.index) #return as string
      
      def calc_left():
            
            
        


class searchtree:

      def __init__(self, items, capacity): #constructor of class

#          self.items = self.insert_root(items)
          self.root = None
          self.n_items = len(items)
          self.best_value = -1
          self.weight = -1
          self.capacity = capacity
          
#      def create_root(self):
#          Item = namedtuple("Item", ['index', 'value', 'weight'])
#          return Item(-1, 0, 0)
          
#      def insert_root(self, items):
#          Item = namedtuple("Item", ['index', 'value', 'weight'])
#          # create dummy item to set the root
#          items_w_root = items
#          items_w_root = [Item(-1, 0, 0)] + items_w_root
#          return items_w_root

          

      def create(self, item, next_item):  #create binary search tree nodes
          print(self.root)
          if self.root == None:
             # this statement creates the root node
             self.root = Node(item)
#
#         
#    # every other iteration will come through this section
#      else:
#         print(self.root)
         current = item

         while 1:
             print(item.weight)
             if item.weight < self.capacity:
            
               print(current.left)
               # if the current left node is non-negative
               if current.left:
                  # now we move to the left most node as the new value is smaller than the current node value
                  current = current.left
               else:
                  # new left child created
                  current.left = Node(next_item)
                  break;      
             
             elif val > current.info:
                print(current.right)
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



# create root node                      
tree = searchtree(items, capacity)     
#arr = [8,3,1,6,4,7,10,14,13]
# create the root node
items = Item(-1, 0, 0) + items
# grow the tree
for idx, item in enumerate(items):
    if idx < len(items)-1:
        tree.create(items[idx], items[idx+1])
    else:
        print("end of the line")
#print('Breadth-First Traversal')
#tree.bft()
#print('Inorder Traversal')
#tree.inorder(tree.root) 
#print('Preorder Traversal')
#tree.preorder(tree.root) 
#print('Postorder Traversal')
#tree.postorder(tree.root)