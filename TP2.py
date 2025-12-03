import TP1

def descent(t, b) :
    if TP1.est_triangolaire_inferieur(t) :
        x = [0 for i in range(len(t))]
        x[0] = b[0] / t[0][0]
        for i in range(1, len(t)) :
            somme = 0
            for j in range(i) :
                somme += t[i][j] * x[j]
            x[i] = (b[i] - somme) / t[i][i]
        return x
    else :
        return "la matrice n'est pas triangolaire inferieur"

def remonte(t, b) :
    if TP1.est_triangolaire_superieur(t) : 
        x = [0 for i in range(len(t))]
        n = len(t) - 1
        x[n] = b[n] / t[n][n]
        for i in range(n - 1, -1, -1) : 
            somme = 0
            for j in range(i + 1, n + 1) :
                somme += t[i][j] * x[j]
            x[i] = (b[i] - somme) / t[i][i]
        return x
    else :
        return "la matrice n'est pas triangolaire superieur"
    
def carmer(t, b) :
    n = len(t)
    x = [0 for i in range(n)]
    det = TP1.determinant(t)
    if det == 0 :
        return "Le système n'a pas de solution "
    for i in range(n):
        copie = [row[:] for row in t]
        for j in range(n):
            copie[j][i] = b[j]
        x[i] =  TP1.determinant(copie) / det
    return x