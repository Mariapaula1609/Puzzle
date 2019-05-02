# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:07:54 2018

@author: eumartinez
"""

from abc import ABC, abstractmethod
from Node import Node


class Problem(ABC):
 
    def __init__(self,initial_state,final_state):
        self.initial_node = Node(initial_state)
        self.final_node = Node(final_state) 
        super().__init__()
    
    @abstractmethod
    def child_node(self,node):
        pass
    

    def goal_test(self,node):
        
        if isinstance(node, Node):
            if self.final_node == node:
                return True
            else:
                return False
        else:
            return False
    
    @property
    def Initial_Node(self):
        # Do something if you want
        return self.initial_node

    @Initial_Node.setter
    def Initial_Node(self,node):
        # Do something if you want
        self.initial_node = node
        
    @property
    def Goal_Node(self):
        # Do something if you want
        return self.goal_node

    @Goal_Node.setter
    def Goal_Node(self,node):
        # Do something if you want
        self.goal_nodee = node
        
    
 