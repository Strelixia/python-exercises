def exercice():
    print("BIENVENU CHEZ NOUS")
    print("saissi la masse de l'objet")
    masse = float(input())
    print("saissi le volume de l'objet")
    volume = float(input())
    densité = masse/volume
    print("la densité est de:",densité)
    if densité > 2400 and densité <=2700:
        print("c'est de l'Aluminium")
    elif densité > 8100 and densité <=8300:
        print("c'est du Bronze")
    elif densité > 10400 and  densité <=10600:
        print("c'est de l'Argent")
    elif densité > 11200 and densité <=11400:
        print("c'est du Plomb")
    elif densité > 17100 and densité <=17500:
        print("c'est de l'Or")
    elif densité > 22000 and densité  <=22500:
        print("c'est du Platine")
exercice()