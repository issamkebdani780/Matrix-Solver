import TP1
import TP2
import TP31
import TP32
import TP33

t = []
b=[]

while True :
    print("#################### Menu ####################")
    print("1- lire matrice ")
    print("2- afficher matrice ")
    print("3- Method directe:  ")

    print("0- exit")

    choix = int(input("entre votre choix : "))
    if choix == 1 :
        t, b = TP1.lire_matrice()
    elif choix == 2 :
        TP1.afficher_matrice(t, b)
    elif choix == 3:
        while True :
            print("########## method direct ##########")
            print("1- carmer ")
            print("2- Gauss pivot non null  ")
            print("3- Gauss pivot partiel  ")
            print("4- Gauss pivot total  ")
            print("0- exit method direct")
            choix2 = int(input("entre type de method : "))
            if choix2 == 1 :
                print(TP2.carmer(t,b))
            elif choix2 == 2 :
                TP31.Gauss_pivot_non_null(t, b)
            elif choix2 == 3 :
                TP32.Gauss_partial(t, b)
            elif choix2 == 4 :
                TP33.Gauss_total(t, b)
            elif choix2 == 0 :
                break    

    elif choix == 0 :
        break