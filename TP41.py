import TP1
import TP2
def decomposition(t,n) :
    print("a = L * U")
    u = [row[:] for row in t]
    id = TP1.matrice_didentite(t)

    for k in range(n):
        p = u[k][k]
        for i in range(k + 1, n) :
            q = u[i][k]
            u[i][k] = 0
            id[i][k] = q/p
            for j in range(k + 1, n) :
                u[i][j] = u[i][j] - u[k][j] * (q/p)
        print(f"--- eteration k = {k + 1} ---")
        print("pivot = ", p)
        print(f"la matrice U{k + 1} ")
        print(u)
        print(f"la matrice L{k + 1}")
        print(id)

    return u, id

def decomposition_recursive(t, n, u=None, l=None, k=0):
    if u is None:
        u = [row[:] for row in t]       
    if l is None:
        l = TP1.matrice_didentite(t)    
    
    if k == n: 
        return u, l
    
    pivot = u[k][k]
    for i in range(k + 1, n):
        q = u[i][k]
        u[i][k] = 0
        l[i][k] = q / pivot
        for j in range(k + 1, n):
            u[i][j] -= q * u[k][j] / pivot
    
    print(f"--- iteration k = {k + 1} ---")
    print("pivot =", pivot)
    print(f"la matrice U{k + 1}")
    print(u)
    print(f"la matrice L{k + 1}")
    print(l)
    
    return decomposition_recursive(t, n, u, l, k + 1)


def decomposition_final(t, b) :
    print("le system est:")
    TP1.afficher_matrice(t, b)

    u, l = decomposition(t, len(t))

    print("la matrice u : ")
    print(u)
    print("la matrice L : ")
    print(l)

    print("------------------2- resodre Ly = b par descente------------------------------------------")
    print("le system reduit:")
    TP1.afficher_matrice(l, b)
    print("le resulta donne: ")
    y = TP2.descent(l, b)
    print(y)

    print("------------------3- resodre Ux = y par remonte ------------------------------------------")
    print("le system reduit:")
    TP1.afficher_matrice(u, y)
    print("le resulta donne: ")
    x = TP2.remonte(u, y)
    return x

def decomposition_final_recursive(t, b):
    print("Le system est:")
    TP1.afficher_matrice(t, b)
    
    u, l = decomposition_recursive(t, len(t))
    
    print("La matrice U :")
    print(u)
    print("La matrice L :")
    print(l)
    
    
    print("------------------ 2- Resoudre Ly = b par descente ------------------")
    print("Le system reduit:")
    TP1.afficher_matrice(l, b)
    y = TP2.descent(l, b)
    print("Resultat y:")
    print(y)
    
    
    print("------------------ 3- Resoudre Ux = y par remonte ------------------")
    print("Le system reduit:")
    TP1.afficher_matrice(u, y)
    x = TP2.remonte(u, y)
    print("Resultat x:")
    print(x)
    
    return x