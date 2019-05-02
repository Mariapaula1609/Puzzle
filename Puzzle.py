from Node import Node
from Problem import Problem
import math

class Puzzle(Problem):
    #constructor
    def __init__(self,initial_state=[],finish_state=[]):
        super().__init__(initial_state,finish_state)
    #funciones
    #generar hijo
    def child_node(self,node):
        child=[]

        son=self.up(node)
        if(son!=None):
            child.append(son)

        son=self.down(node)
        if(son!=None):
            child.append(son)

        son=self.right(node)
        if(son!=None):
            child.append(son)

        son=self.left(node)
        if(son!=None):
            child.append(son)

        return child

    #operaciones
    def up(self,node):
        state=node.State[:]
        tamanio=len(state)
        dimension=int(math.sqrt(tamanio))
        #busco el en que lugar esta el vacio
        indiceVacio=state.index(0)

        if((indiceVacio+dimension)>tamanio-1):
            return None
        else:
            #intercambio a el vacio con la ficha a mover
            aux=state[indiceVacio]
            state[indiceVacio]=state[indiceVacio+(dimension)]
            state[indiceVacio+(dimension)]=aux
            new_node=Node(state,parent=node,action='up')
            return new_node

    def down(self,node):
        #copio la lista
        state=node.State[:]
        tamanio=len(state)
        dimension=int(math.sqrt(tamanio))
        #busco el en que lugar esta el vacio
        indiceVacio=state.index(0)
        #print("indice: "+str(indiceVacio))
        if((indiceVacio-dimension)<0):
            return None
        else:
            #intercambio a el vacio con la ficha a mover
            aux=state[indiceVacio]
            state[indiceVacio]=state[indiceVacio-(dimension)]
            state[indiceVacio-(dimension)]=aux
            new_node=Node(state,parent=node,action='down')
            return new_node

    def multipleRight(self,indice,n,tamanio):
        i = 2
        multiple = 0
        while i < (tamanio - n):
            multiple = n * i
            if (multiple > (indice + 1)):
                return ((i - 1) * n)
            i = i + 1

    def multipleLeft(self,indice,n,tamanio):
        i = 2
        multiple = 0
        while i < tamanio:
            multiple = n * i
            if (multiple > (indice + 1)):
                return ((i - 1) * n)
            i = i + 1

    def right(self,node):
        state=node.state[:]
        tamanio=len(state)
        dimension=int(math.sqrt(tamanio))
        #busco el en que lugar esta el vacio
        indiceVacio=state.index(0)
        #validar que vacio no este en la primera columna
        multiple = self.multipleRight(indiceVacio,dimension,tamanio)
        if(multiple == indiceVacio):
            return None
        else:
            #Intercambia
            aux = state[indiceVacio]
            state[indiceVacio] = state[indiceVacio - 1]
            state[indiceVacio - 1] = aux
            new_node=Node(state,parent=node,action='right')
            return new_node

    def left(self,node):
        state=node.state[:]
        tamanio=len(state)
        dimension=int(math.sqrt(tamanio))
        #busco el en que lugar esta el vacio
        indiceVacio=state.index(0)
        #validar que vacio no este en la primera columna
        multiple = self.multipleLeft(indiceVacio,dimension,tamanio)
        if((multiple - 1) == indiceVacio):
            return None
        else:
            #Intercambia
            aux = state[indiceVacio]
            state[indiceVacio] = state[indiceVacio + 1]
            state[indiceVacio + 1] = aux
            new_node=Node(state,parent=node,action='left')
            return new_node
#pz = Puzzle()
#print(pz.multipleRight(3,3,9))
