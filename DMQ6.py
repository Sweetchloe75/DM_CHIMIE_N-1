import matplotlib.pyplot as plt

""" initialisation des données"""
# nombres steochiométriques des 2 réactifs
sto1 = 1
sto2 = 1

# premier réactif: le réactif titré
C1 = 0.1 * 10 ** 3
V1 = 10 * 10 ** -6  # V1 sera en m3
# 2nd réactif: le réactif titrant
C2 = 0.1012 * 10 ** 3
V2max = 25  # en m3, volume max de solution titrante
Veau = 0  # volume d'eau distillée
# conductivités molaires ioniques limites
l1 = 7.3
l2 = 19.9
l3 = 5.0
l4 = 7.6


# boucle permettant de calculer la quantité de matière de chaques ions en fonction du Volume versé
for V in range(V2max + 1):
    # convertit V de mL en m3
    V = V * 10 ** -6
    # Pour chaque ajout de V2,calcul des quantités de matière initiales:
    n1_ini = C1 * V1
    n2_ini = C2 * V
    n3 = C2 * V
    n4 = C1 * V1

    # détermination de xmax
    if n1_ini / sto1 > n2_ini / sto2:
        # réactif 2 limitant
        xmax = n2_ini / sto2
    else:
        xmax = n1_ini / sto1
        # réactif 1 limitant
    # Calcul des quantités finales des réactifs
    # si n<0, c'est que n=0
    n1_fin = n1_ini - sto1 * xmax
    if n1_fin < 0:
        n1_fin = 0
    n2_fin = n2_ini - sto2 * xmax
    if n2_fin < 0:
        n2_fin = 0
    # calcul des quantités en quantité de matière
    C_HO = n2_fin / (V + Veau + V1)  # concentration en H0- en mol/m3
    C_NH4 = n2_fin / (V + Veau + V1)  # concentration en NH4+ en mol/m3
    C_Na = n3 / (V + Veau + V1)  # concentration en Na+ en mol/m3
    C_Cl = n4 / (V + Veau + V1)  # concentration en Cl- en mol/m3
    conductivite = C_HO * l2 + C_NH4 * l1 + C_Na * l3 + C_Cl * l4

    # affichage des points sur une courbe
    plt.plot(V, conductivite, "rx")

# FIN  DE LA BOUCLE ###############

# axes du graphe
plt.xlabel("Volume V de solution titrante versée en m3")
plt.ylabel("Conductivité en mS")
plt.title("Titrage de NH4Cl par NaOH - question Q6")

# affichage de la fenêtre
plt.show()
