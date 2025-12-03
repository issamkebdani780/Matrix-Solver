from TP1 import *

def triangularisation_partielle(t, b) :
    n = len(t)
    
    for k in range(n) :
        p = t[k][k]
        l = k
        for i in range(k, n) :
            if abs(t[i][k] )> p :
                p = t[i][k]
                l = i
        if l != k :
            change_ligne(t, k, l)
            b[k] , b[l] = b[l], b[k]
        for i in range(k + 1, n) :    
            print("iteration i =",i)   
            q = t[i][k]
            t[i][k] = 0
            b[i] = b[i] - (q / p) * b[k]
            for j in range(k + 1, n) :
                t[i][j] = t[i][j] - t[k][j] * (q / p)    
            afficher_matrice(t)
            print(b)     
    return t, b

def Gauss_partial(t, b) :
    print("le sysstem est: ")
    afficher_matrice(t)
    print(b)
    t, b= triangularisation_partielle(t, b)
    print("le matrice reduit est: ")
    afficher_matrice(t)
    print(b)
    print("le resulta donne: ")
    print(remonte(t, b))

t = [[1, 6, 9], [2, 1, 2], [3, 6, 9]]
b = [1, 2, 3]
Gauss_partial(t, b)