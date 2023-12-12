from Productes import Producte
import sys

print("=================================")
print("TEST CLASS PRODUCTE:")
print("=================================")

print("TEST 1: CREAR PRODUCTES QUE PUGUIN EXISTIR\nResultat:", end= " ")
pr1_codi = "0000A"
pr2_nom = "samarreta"
pr3_preu = 15.99
pr4_des = "Descripció sobre jaqueta"
try:
    pr1 = Producte(pr1_codi, "pantalons", "12.99", "Descripció sobre pantalons")
    pr2 = Producte("0000B", pr2_nom, 13, "Descripció sobre samarreta")
    pr3 = Producte("0000C", "camisa", pr3_preu, "Descripció sobre camisa")
    pr4 = Producte("0000D", "jaqueta", 20 + 1.99, pr4_des)

    # Comprovem que els diversos atributs estiguin ben implementats dintre les instàncies
    assert(pr1.codi==pr1_codi)
    assert(pr2.nom==pr2_nom)
    assert(pr3.preu==pr3_preu)
    assert(pr4.descripcio==pr4_des)
except:
    print("Productes no creats [ERROR]")
    sys.exit()
else:
    print("Productes creats correctament [OK]")

print("=================================")
print("TEST 2: CREAR UN FALS PRODUCTE\nResultat:", end= " ")
try:
    prf = Producte("0001A", "Pantalons falsos", "preu evidentment fals", "Descripció falsa")
except:
    print("Producte no creat [OK]")
else:
    print("Producte creat [ERROR]")
    sys.exit()
