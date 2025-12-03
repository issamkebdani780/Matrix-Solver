from TP1 import *

def triangularisation_totalle(t, b) :
    n = len(t)
    x = [i for i in range(n)]
    for k in range(n) :
        p = t[k][k]
        l1 = k
        l2 = k
        for i in range(k, n) :
            for s in range(k, n) :
                if t[i][s] > p  :
                    p = t[i][s]
                    l1 = i
                    l2 = s
        if l1 != k :
            change_ligne(t, k, l1)
            b[k], b[l1] = b[l1], b[k]
        if l2 != k :
            change_column(t, k, l2)
            x[k], x[l2] = x[l2], x[k]    
        for i in range(k + 1, n) :    
            print("iteration i =",i)   
            q = t[i][k]
            t[i][k] = 0
            b[i] = b[i] - (q / p) * b[k]
            for j in range(k + 1, n) :
                t[i][j] = t[i][j] - t[k][j] * (q / p)    
            afficher_matrice(t)
            print(b)     
    return t, b, x

def Gauss_total(t, b) :
    print("le matrice A est: ")
    afficher_matrice(t)
    print("le vacteur b ets :")
    print(b)
    t, b, x = triangularisation_totalle(t, b)
    print("le matrice reduit est: ")
    afficher_matrice(t)
    print(b)
    x1 = remonte(t, b)
    print("le resulta donne: ")
    x_final = [0 for i in range(len(x)) ]
    for i in range(len(x)) :
        x_final[i] = x1[x[i]] 
    print(x_final)




t = [[1, 3, 3], [2, 2, 5], [3, 2, 6]]
b = [-2, 7, 12]
Gauss_total(t, b)
