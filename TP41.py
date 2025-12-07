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
    print(x)