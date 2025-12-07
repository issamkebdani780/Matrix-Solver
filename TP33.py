import TP1
import TP2

def triangularisation_totalle(t, b):
    n = len(t)
    x = [i for i in range(n)]

    for k in range(n):
        p = abs(t[k][k])
        l1, l2 = k, k

        for i in range(k, n):
            for j in range(k, n):
                if abs(t[i][j]) > p:
                    p = abs(t[i][j])
                    l1, l2 = i, j

        if l1 != k:
            TP1.change_ligne(t, k, l1)
            b[k], b[l1] = b[l1], b[k]

        if l2 != k:
            TP1.change_column(t, k, l2)
            x[k], x[l2] = x[l2], x[k]

        if t[k][k] == 0:
            raise ValueError("Pivot nul même après pivot total !")
        
        for i in range(k+1, n):
            q = t[i][k] / t[k][k]
            t[i][k] = 0
            b[i] -= q * b[k]

            for j in range(k+1, n):
                t[i][j] -= q * t[k][j]

        print(f"iteration {k+1} :")
        TP1.afficher_matrice(t, b)

    return t, b, x

def triangularisation_totalle_recursive(t, b, x=None, k=0):
    n = len(t)
    
    if x is None:
        x = list(range(n))  
    
    if k == n:
        return t, b, x

    p = abs(t[k][k])
    l1, l2 = k, k
    for i in range(k, n):
        for j in range(k, n):
            if abs(t[i][j]) > p:
                p = abs(t[i][j])
                l1, l2 = i, j  
    
    if l1 != k:
        TP1.change_ligne(t, k, l1)
        b[k], b[l1] = b[l1], b[k]
    
    if l2 != k:
        TP1.change_column(t, k, l2)
        x[k], x[l2] = x[l2], x[k]

    if t[k][k] == 0:
        return "Pivot nul même après pivot total !"
    
    for i in range(k + 1, n):
        q = t[i][k] / t[k][k]
        t[i][k] = 0
        b[i] -= q * b[k]
        for j in range(k + 1, n):
            t[i][j] -= q * t[k][j]
    
    print(f"iteration {k + 1} :")
    TP1.afficher_matrice(t, b)
    
    return triangularisation_totalle_recursive(t, b, x, k + 1)



def Gauss_total(t, b):
    print("La matrice A est :")
    TP1.afficher_matrice(t, b)

    t, b, x = triangularisation_totalle(t, b)

    print("La matrice réduite est :")
    TP1.afficher_matrice(t, b)

    x1 = TP2.remonte(t, b)

    print("Le résultat donne :")
    x_final = [0 for _ in range(len(x))]
    for i in range(len(x)):
        x_final[i] = x1[x[i]]

    print(x_final)

def Gauss_total_recursive(t, b):
    print("La matrice A est :")
    TP1.afficher_matrice(t, b)

    t, b, x = triangularisation_totalle_recursive(t, b)

    print("La matrice réduite est :")
    TP1.afficher_matrice(t, b)

    x1 = TP2.remonte(t, b)

    print("Le résultat donne :")
    x_final = [0 for _ in range(len(x))]
    for i in range(len(x)):
        x_final[i] = x1[x[i]]

    print(x_final)
