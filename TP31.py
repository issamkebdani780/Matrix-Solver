import TP1
import TP2

def triangularisation(t, b):
    n = len(t)
    for i in range(n - 1) :
        pivot = t[i][i]
        if pivot != 0 : 
            for j in range(i + 1, n) :
                q = t[j][i] / pivot
                t[j][i] = 0
                for k in range(i + 1 , n) :
                    t[j][k] = t[j][k] - q  * t[i][k]
                b[j] = b[j] - q * b[i]
        else : 
            return "detareminat is null"
    return t, b

def Gauss_pivot_non_null(t,b) : 
    print("le system est: ")
    TP1.afficher_matrice(t,b)
    t_trin, b_trian = triangularisation(t,b) 
    print("le matrice reduit est: ")
    TP1.afficher_matrice(t_trin, b_trian)
    print("le resulta donne: ")
    print(TP2.remonte(t_trin, b_trian))
