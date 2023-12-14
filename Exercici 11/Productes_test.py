import sys
from Productes import Producte

print("=================================")
print("TEST CLASS PRODUCTE:")
print("=================================")

print("TEST 1: CREAR PRODUCTES QUE PUGUIN EXISTIR\nResultat:", end=" ")
PR1_CODI = "0000A"
PR2_NOM = "samarreta"
PR3_PREU = 15.99
PR4_DES = "Descripció sobre jaqueta"
try:
    pr1 = Producte(
        PR1_CODI, "pantalons", "12.99", "Descripció sobre pantalons"
    )
    pr2 = Producte("0000B", PR2_NOM, 13, "Descripció sobre samarreta")
    pr3 = Producte("0000C", "camisa", PR3_PREU, "Descripció sobre camisa")
    pr4 = Producte("0000D", "jaqueta", 20 + 1.99, PR4_DES)

    # Comprovem que els diversos atributs estiguin ben implementats dintre les
    # instàncies
    assert pr1.codi == PR1_CODI
    assert pr2.nom == PR2_NOM
    assert pr3.preu == PR3_PREU
    assert pr4.descripcio == PR4_DES
except Exception:  # pylint: disable=bare-except
    print("Productes no creats [ERROR]")
    sys.exit()
else:
    print("Productes creats correctament [OK]")

print("=================================")
print("TEST 2: CREAR UN FALS PRODUCTE\nResultat:", end=" ")
try:
    prf = Producte(
        "0001A",
        "Pantalons falsos",
        "preu evidentment fals",
        "Descripció falsa",
    )
except Exception:  # pylint: disable=bare-except
    print("Producte no creat [OK]")
else:
    print("Producte creat [ERROR]")
    sys.exit()
