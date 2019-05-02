# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:29:57 2018

@author: eumartinez
"""


class Node():
 
    def __init__(self,state,parent=None,action=None,path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        super().__init__()
    
    
        
    def __eq__(self, other):

        if isinstance(other, Node):
         
            if self.state == other.State:
                
                return True
            else:
              
                return False
        else:
            return False
    

    def __hash__(self):
        return hash(self.state)

    
    @property
    def State(self):
        # Do something if you want
        return self.state

    @State.setter
    def State(self,state):
        # Do something if you want
        self.state = state
    
    @property
    def Parent(self):
        # Do something if you want
        return self.parent

    @Parent.setter
    def Parent(self,node):
        # Do something if you want
        self.parent = node
        
    @property
    def Action(self):
        # Do something if you want
        return self.action

    @Action.setter
    def Action(self,label):
        # Do something if you want
        self.action = label
        
