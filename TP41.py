from TP1 import *
def decomposition(t,n) :
    print("a = L * U")
    print("le matrice U0")
    u = [row[:] for row in t]
    afficher_matrice(u)
    print("le matrice L0")
    id = matrice_didentite(t)
    for k in range(n):
        print(f'iteration k = ${k}')
        p = u[k][k]
        print(f'pivot  = ${p}')
        for i in range(k + 1, n) :
            q = u[i][k]
            u[i][k] = 0
            id[i][k] = q/p
            for j in range(k + 1, n) :
                u[i][j] = u[i][j] - u[k][j] * (q/p)
        print(f'matrice u${k}')
        afficher_matrice(u)
        print(f'matrice L${k}')
        afficher_matrice(id)
    return u, id


t = [[1,2,3],[1,1,2],[1,1,1]]
b=[2,0,1]


def decomposition_final() :
    print("le system est:")
    afficher_matrice(t)
    print(b)
    u, l = decomposition(t,3)
    print("la matrice u : ")
    afficher_matrice(u)
    print("la matrice L : ")
    afficher_matrice(l)
    print("------------------2- resodre Ly = b par descente------------------------------------------")
    print("le system reduit:")
    afficher_matrice(l)
    print(b)
    print("le resulta donne: ")
    y = descent(l, b)
    print(y)
    print("------------------3- resodre Ux = y par remonte ------------------------------------------")
    print("le system reduit:")
    afficher_matrice(u)
    print(y)
    print("le resulta donne: ")
    print(remonte(u, y))




decomposition_final()