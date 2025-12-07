import TP1
import TP2

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
            TP1.change_ligne(t, k, l)
            b[k] , b[l] = b[l], b[k]
        for i in range(k + 1, n) :    
            q = t[i][k]
            t[i][k] = 0
            b[i] = b[i] - (q / p) * b[k]
            for j in range(k + 1, n) :
                t[i][j] = t[i][j] - t[k][j] * (q / p)   
        print(f"eteration {k + 1} : ")
        TP1.afficher_matrice(t, b)           
    return t, b

def triangularisation_partielle_recursive(t, b, k = 0) :
    n = len(t)
    if k == n :
        return t, b
    
    p = abs(t[k][k])
    l = k
    for i in range(k, n):
        if abs(t[i][k]) > p:
            p = abs(t[i][k])
            l = i
    if l != k:
        TP1.change_ligne(t, k, l)
        b[k], b[l] = b[l], b[k]

    pivot = t[k][k]

    for i in range(k + 1, n):
        q = t[i][k]
        t[i][k] = 0
        b[i] = b[i] - (q / pivot) * b[k]
        for j in range(k + 1, n):
            t[i][j] = t[i][j] - t[k][j] * (q / pivot)
    
    print(f"iteration {k + 1} : ")
    TP1.afficher_matrice(t, b)
    
    
    return triangularisation_partielle_recursive(t, b, k + 1)



def Gauss_partial(t, b) :
    print("le sysstem est: ")
    TP1.afficher_matrice(t, b)
    t, b= triangularisation_partielle(t, b)
    print("le matrice reduit est: ")
    TP1.afficher_matrice(t, b)
    print("le resulta donne: ")
    print(TP2.remonte(t, b))

def Gauss_partial_recursive(t, b) :
    print("le sysstem est: ")
    TP1.afficher_matrice(t, b)
    t, b= triangularisation_partielle_recursive(t, b)
    print("le matrice reduit est: ")
    TP1.afficher_matrice(t, b)
    print("le resulta donne: ")
    print(TP2.remonte(t, b))
