# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:30:54 2018

@author: eumartinez
"""
from Node import Node
from Problem import Problem

class WaterJug(Problem):

    def __init__(self,quantity_A=4,quantity_B=3,initial_state=(0,0),final_state=(2,0)):
        self.quantity_A=quantity_A
        self.quantity_B=quantity_B
        super().__init__(initial_state,final_state)

    def child_node(self,node):
        child=[]
        son=self.fill_A(node)
        if(son!=None):
            child.append(son)

        son=self.fill_B(node)
        if(son!=None):
            child.append(son)

        son=self.empty_A(node)
        if(son!=None):
            child.append(son)

        son=self.empty_B(node)
        if(son!=None):
            child.append(son)

        son=self.Pour_B_A(node)
        if(son!=None):
            child.append(son)

        son=self.Pour_A_B(node)
        if(son!=None):
            child.append(son)

        return child

    def fill_A(self,node):
        state=node.State
        if(state[0]<4):
            new_state=(4,state[1])
            new_node=Node(new_state,parent=node,action='fill_A')
            return new_node
        else:
            return None

    def fill_B(self,node):
        state=node.State
        if(state[1]<3):
            new_state=(state[0],3)
            new_node=Node(new_state,parent=node,action='fill_B')
            return new_node
        else:
            return None

    def empty_A(self,node):
        state=node.State
        if(state[0]>0):
            new_state=(0,state[1])
            new_node=Node(new_state,parent=node,action='empty_A')
            return new_node
        else:
            return None

    def empty_B(self,node):
        state=node.State
        if(state[1]>0):
            new_state=(state[0],0)
            new_node=Node(new_state,parent=node,action='empty_B')
            return new_node
        else:
            return None

    def Pour_B_A(self,node):
        state=node.State
        if(state[0]<4):
            val=state[1]-(4-state[0])
            if val>0:
                new_state=(4,val)
            else:
                new_state=(state[0]+state[1],0)
            new_node=Node(new_state,parent=node,action='Pour_B_A')
            return new_node
        else:
            return None

    def Pour_A_B(self,node):
        state=node.State
        if(state[1]<3):
            val=state[0]-(3-state[1])
            if val>0:
                new_state=(val,3)
            else:
                new_state=(0,state[0]+state[1])
            new_node=Node(new_state,parent=node,action='Pour_A_B')
            return new_node
        else:
            return None
