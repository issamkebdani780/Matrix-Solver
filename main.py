import TP1
import TP2
import TP31
import TP32
import TP33
import TP41
import Tp42
import Tp5

t = []
b=[]

while True :
    print("#################### Menu ####################")
    print("1- lire matrice ")
    print("2- afficher matrice ")
    print("3- Method directe:  ")
    print("4- Method iterative:  ")
    print("0- exit")

    choix = int(input("entre votre choix : "))
    if choix == 1 :
        t, b = TP1.lire_matrice()
    elif choix == 2 :
        TP1.afficher_matrice(t, b)
    elif choix == 3:
        while True :
            print("########## method direct ##########")
            print("1- carmer iterative ")
            print("2 - carmer recursive ")
            print("3- Gauss pivot non null iterative")
            print("4 - Gauss pivot non null recursive")
            print("5- Gauss pivot partiel iterative")
            print("6- Gauss pivot partiel recursive")
            print("7- Gauss pivot total iterative")
            print("8- Gauss pivot total recursive")
            print("9- Decomposition LU iterative")
            print("10- Decomposition LU recursive")
            print("11- Gauss Jordan iterative")
            print("12- Gauss Jordan recursive")
            print("0- exit ")
            choix2 = int(input("entre type de method : "))
            if choix2 == 1 :
                print(TP2.carmer(t,b))
            elif choix2 == 2 :
                print(TP2.carmer_recursive(t, b))
            elif choix2 == 3 :
                TP31.Gauss_pivot_non_null(t ,b)
            elif choix2 == 4 :
                TP31.Gauss_pivot_non_null_recursive(t, b)
            elif choix2 == 5:
                TP32.Gauss_partial(t,b)
            elif choix2 == 6:
                TP32.Gauss_partial_recursive(t, b)
            elif choix2 == 7:
                TP33.Gauss_total(t, b)
            elif choix2 == 8:
                TP33.Gauss_total_recursive(t, b)
            elif choix2 == 9:
                print(TP41.decomposition_final(t, b))
            elif choix2 == 10:
                print(TP41.decomposition_final_recursive(t, b))
            elif choix2 == 11:  
                print(Tp42.gauss_jordan(t, b))
            elif choix2 == 12:
                print(Tp42.gauss_jorda_recursive(t, b))
            elif choix2 == 0:
                break
    elif choix == 4:
        while True: 
            print("########## method iterative ##########")
            print("1- jacobi ")
            print("3- gauss seidel ")
            print("0- exit ")
            choix3 = int(input("entre type de method : "))
            if choix3 == 1:
                print("la solution est : ")
                print(Tp5.jacobi(t, b))
            elif choix3 == 3:
                print("la solution est : ")
                print(Tp5.gauss_seidel(t, b))
            elif choix3 == 0:
                break
    elif choix == 0 :
        break