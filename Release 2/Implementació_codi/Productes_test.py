from Productes import Producte

print("=================================")
print("TEST CLASS PRODUCTE:")

errors = 0

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
    errors+=1
else:
    print("Productes creats correctament [OK]")

print("=================================")
print("TEST 2: CREAR UN FALS PRODUCTE (preu fals)\nResultat:", end=" ")
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
    errors+=1

print("=================================")
print("TEST 3: VALORAR UN PRODUCTE\nResultat:", end=" ")
valoracio = ["Asiel","45369724K", 4, "Bona qualitat"]
try:
    prv = Producte("0000B", "samarreta", 13, "Descripció sobre samarreta")
    prv.valora(valoracio[0],valoracio[1],valoracio[2])

    # Comprovem que els elements de la valoració estan on pertoca
    assert(prv.valoracions[0][0]==valoracio[0])
    assert(prv.valoracions[0][1]==valoracio[1])
    assert(prv.valoracions[0][2]==valoracio[2])
except Exception:  # pylint: disable=bare-except
    print("Producte no creat o atributs incorrectes [ERROR]")
    errors+=1
else:
    print("Producte creat [OK]")

print("=================================")
print("TEST 4: VALORAR UN PRODUCTE MALAMENT\n")
vf1 = ["Joel","76942050F", 40, "M'ha encantat molt"]
vf2 = ["David","47681247M", -2, "M'ha encantat molt poc"]
vf3 = ["Guillem","47970268", 2.5, "Meh"]
vf4 = ["David", "47681247M","Super bona peça", 5]

print("\n-> Test 4.1: introduïr un nombre superior a 5\nResultat:", end=" ")
try:
    prvf = Producte("0000B", "samarreta", 13, "Descripció sobre samarreta")
    prvf.valora(vf1[0], vf1[1], vf1[2], vf1[3])
except Exception:  # pylint: disable=bare-except
    print("Producte no creat [OK]")
else:
    print("Producte creat [ERROR]")
    errors+=1

print("\n-> Test 4.2: introduïr un nombre negatiu\nResultat:", end=" ")
try:
    prvf = Producte("0000B", "samarreta", 13, "Descripció sobre samarreta")
    prvf.valora(vf2[0], vf2[1], vf2[2], vf2[3])
except Exception:  # pylint: disable=bare-except
    print("Producte no creat [OK]")
else:
    print("Producte creat [ERROR]")
    errors+=1

print("\n-> Test 4.3: introduïr un nombre tipus float\nResultat:", end=" ")
try:
    prvf = Producte("0000B", "samarreta", 13, "Descripció sobre samarreta")
    prvf.valora(vf3[0], vf3[1], vf3[2], vf3[3])
except Exception:  # pylint: disable=bare-except
    print("Producte no creat [OK]")
else:
    print("Producte creat [ERROR]")
    errors+=1

print("\n-> Test 4.4: introduïr un string\nResultat:", end=" ")
try:
    prvf = Producte("0000B", "samarreta", 13, "Descripció sobre samarreta")
    prvf.valora(vf4[0], vf4[1], vf4[2], vf4[3])
except Exception:  # pylint: disable=bare-except
    print("Producte no creat [OK]")
else:
    print("Producte creat [ERROR]")
    errors+=1


if not errors:
    print("=================================")
    print("Test superat sense errors")
    print("=================================")
else: 
    print("=================================")
    print("Test amb", errors, "error(s)")
    print("=================================")