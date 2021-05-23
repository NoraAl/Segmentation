import numpy as np
import math

# import networkx as nx

# G graph 
# d_v degree of vertex v
# L(u,v) --> d_v if u-v connected,      -1 if adjacent,     0 otherwise
# T degree matrix
# Laplacian (£)
# A = np.array([[0, 1, 1, 1], [0, 0, 1, 1], [0,0,0,1], [0,0,0,0]])
A = np.array([[0, 1, 1, 1], [0, 0, 1, 1], [0,0,0,1], [1,0,0,0]])
D = None
L = None
laplacian_l = None
laplacian = None
# LL = np.array([[]])
# TT = np.array([[1,4], [9, 16]], dtype = np.float)
# print(TT)

def degree(A = A):
    global D
    D = np.diag(np.sum(A, axis=1))


def get_L():
    global L
    L = D - A


def laplacian_():
    DD = np.sqrt(np.reciprocal(D))
    temp = DD * L * DD 
    global laplacian 
    laplacian = temp


def laplacian_loop():
    temp = np.array(L, dtype=np.float)
    temp.fill(0)
    for i, x in np.ndenumerate(D):
        # print (i)
        u = i[0]
        v = i[1]
        
        # temp[u,v] = 0
        if (L[u,v]!= 0): # if they are adjacent
            if (u == v):
                if (D[u,v] != 0):
                    temp[u,v] = 1
            else:
                a = math.sqrt(D[u,u] * D[v,v])
                if (a!= 0):
                    temp[u,v] = -1.0 / a
        global laplacian_l
        laplacian_l = temp
        


def main():
    print ('A:\n', A, '\n')
    
    degree()
    print ('D:\n', D, '\n')
    
    get_L()
    print ('L:\n', L, '\n')

    laplacian_()
    print ('Lap:\n', laplacian, '\n')

    laplacian_loop()
    print ('Lap_:\n', laplacian_l, '\n')


main()
