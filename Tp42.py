def gauss_jordan(t, b) :
    for k in range(len(t)) :
        p = t[k][k]
        for j in range(len(t)):
            t[k][j] = t[k][j] / p
        for i in range(len(t)) :
            if i != k :
                q = t[i][k]
                t[i][k] = 0
                for j in range(k + 1, len(t)):
                    t[i][j] = t[i][j] - (q/p) * t[k][j]
