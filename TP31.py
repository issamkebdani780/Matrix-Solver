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
        print(f"eteration {i + 1} : ")
        TP1.afficher_matrice(t, b)
    return t, b

def triangularisation_recursive(t, b, i = 0) :
    n = len(t)
    if i == n -1 :
        return t, b
    pivot = t[i][i]
    if pivot == 0 : 
        return "detareminat is null"
    lo(t, b, i, n , pivot)
    return triangularisation_recursive(t, b, i + 1)
    
    
def lo(t, b, i, n, pivot) :
    for j in range(i + 1, n) :
        q = t[j][i] / pivot
        t[j][i] = 0
        for k in range(i + 1 , n) :
            t[j][k] = t[j][k] - q  * t[i][k]
        b[j] = b[j] - q * b[i]    


def Gauss_pivot_non_null(t,b) : 
    print("le system est: ")
    TP1.afficher_matrice(t,b)
    t_trin, b_trian = triangularisation(t,b) 
    print("le matrice reduit est: ")
    TP1.afficher_matrice(t_trin, b_trian)
    print("le resulta donne: ")
    print(TP2.remonte(t_trin, b_trian))

def Gauss_pivot_non_null_recursive(t,b) : 
    print("le system est: ")
    TP1.afficher_matrice(t,b)
    t_trin, b_trian = triangularisation_recursive(t,b) 
    print("le matrice reduit est: ")
    TP1.afficher_matrice(t_trin, b_trian)
    print("le resulta donne: ")
    print(TP2.remonte(t_trin, b_trian))
