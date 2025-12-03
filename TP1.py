def lire_matrice() :
    n = int(input("entre la taile de matrice: "))   
    t = [[0 for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n) :
        for j in range(0,n) :
            t[i][j] = int(input("T[%d][%d] = "%(i, j)))
    print("les valeur de vacteur b: ")
    b = [0 for i in range(n)]
    for i in range(0, n) :
        b[i] = int(input("b[%d] = " %i))
    return t, b

def afficher_matrice(t, b) :
    n = len(t)
    for i in range(0, n) :
        for j in range(0, n) :
            print(t[i][j], end=" ")
        print(" | ",(b[i]))
        print()

def matrice_didentite(t) :
    n = len(t)

    iden = [[0 for i in range(0,n)] for j in range(0, n)]
    for i in range(0, n) :
        for j in range(0, n) :
            if i == j :
                iden[i][j] = 1
            else :
                iden[i][j] = 0 
    afficher_matrice(iden, [0]*n)
    return iden

def somme_matrice(t1, t2):
    if(len(t1) != len(t2)) or (len(t1[0]) != len(t2[0])) :
        print("la taille de t1 n'est pas egale t2!")
        return
    else : 
        n = len(t1)
        somme = [[0 for i in range(0, n)] for j in range(0,n)]
        for i in range(0, n) :
            for j in range(0, n) :
                somme[i][j] = t1[i][j] + t2[i][j]
        afficher_matrice(somme, [0]*n)
        return somme

def prouduit_matrice(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    m1 = len(t1[0])
    m2 = len(t2[0])
    if m1 != n2 : 
        print("ne peut pas calculer le prouduit")
    else :
        prou = [[0 for i in range(0, m2)] for j in range(0, n1)]
        for i in range(0, n1):
            for j in range(0, m2) :
                somme = 0
                for k in range(0, n2):
                    somme += t1[i][k] * t2[k][j]
                prou[i][j] = somme
        afficher_matrice(prou, [0]*n1)
        return prou

def transpose(t) :
    n = len(t)
    trans = [[0 for i in range(n)] for j in range(n)]
    for i in range (n) :
        for j in range(n) :
            trans[i][j] = t[j][i]
    afficher_matrice(trans, [0]*n)
    return trans

def est_triangolaire_superieur(t) :
    n = len(t)
    for i in range(n) :
        for j in range(n) :
            if i > j and t[i][j] != 0 :
                return False
    return True
    
def est_triangolaire_inferieur(t) :
    n = len(t)
    for i in range(n) :
        for j in range(n) :
            if i < j and t[i][j] != 0 :
                return False
    return True

def est_diagonale(t) :
    return est_triangolaire_inferieur(t) and est_triangolaire_superieur(t)

def est_symetrique(t):
    n = len(t)
    for i in range(n) :
        for j in range(n) :
            if (t[i][j] != t[j][i]) :
                return False
    return True

def change_ligne(t,n1,n2) :
    if n1 > len(t) or n2 > len(t) :
        print("entere correct ligne")
    else : 
        m = len(t[0])
        for j in range(m) :
            t[n1][j], t[n2][j] = t[n2][j], t[n1][j]
        return t

def change_column(t,m1,m2) :
    if m1 > len(t[0]) or m2 > len(t[0]) :
        print("entere correct columne")
    else :
        n = len(t)
        for j in range(n) :
            t[j][m1], t[j][m2] = t[j][m2] , t[j][m1]
        return t

def trace(t1) :
    n1 = len(t1)
    trace = 0
    for i in range(0, n1) :
        for j in range(0, n1) :
            if i == j :
                trace += t1[i][j]
    return trace
                
def determinant(t) :
    n = len(t)
    if n == 1 :
        return t[0][0]
    elif n == 2 :
        return t[0][0]*t[1][1] - t[0][1]*t[1][0]
    else :
        det = 0
        for i in range(n) :
            minor = [row[:i] + row[i+1:] for row in t[1:]]
            det += ((-1) ** (i)) * t[0][i] * determinant(minor)
        return det             