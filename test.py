# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:12:28 2018

@author: eumartinez
"""

from BreadthFirst import BreadthFirst
from WaterJug import WaterJug
from Puzzle import Puzzle

pz=Puzzle([1,2,3,8,6,0,7,5,4],[1,2,3,8,0,4,7,6,5])

#wj=WaterJug(4,3,(4,3),(2,0))

#wj=WaterJug()
bf=BreadthFirst(pz)

#bf=BreadthFirst(wj)

sol=bf.run()
print('Solution: '+str(sol))
