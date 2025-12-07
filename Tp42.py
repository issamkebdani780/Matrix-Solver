def gauss_jordan(t, b):
    n = len(t)

    for k in range(n):
        p = t[k][k]

        for j in range(n):
            t[k][j] /= p
        b[k] /= p

        for i in range(n):
            if i != k:
                q = t[i][k]
                for j in range(n):
                    t[i][j] -= q * t[k][j]
                b[i] -= q * b[k]
    return b

def matrice_inveres(t):
    n = len(t)

    for k in range(n):
        p = t[k][k]

        for j in range(2 * n):
            t[k][j] /= p
        
        for i in range(n):
            if i != k:
                q = t[i][k]
                for j in range(2 * n):
                    t[i][j] -= q * t[k][j]
    return t
