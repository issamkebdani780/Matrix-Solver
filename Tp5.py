def jacobi(t, b, Nmax=100):
    n = len(t)  
    x= [0]*n
    for k in range(Nmax):
        
        for i in range(n):
            somme = 0
            for j in range(n):
                if j != i:
                    somme += t[i][j] * x[j]

            x[i] = (b[i] - somme) / t[i][i]
    return x

def gauss_seidel(t, b, Nmax=100):
    n = len(t)
    x = [0]*n
    for k in range(Nmax):
        for i in range(n):
            somme1 = 0
            for j in range(i) :
                somme1 += t[i][j] * x[j]
            somme2 =0 
            for j in range(i+1, n):
                somme2+= t[i][j] * x[j]
            x[i] = (b[i] - somme1 - somme2) / t[i][i]
    return x