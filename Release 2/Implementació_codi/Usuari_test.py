from datetime import date
import Usuari as usr
import Productes as pr

print("############################")
print("TEST CLASS USUARI:")
print("############################")

usr1 = usr.Usuari(
    "47970268L",
    "Guillem",
    "Garcia Dausà",
    "ggarciadausa@gmail.com",
    "contrasenya123",
)
usr2 = usr.Usuari(
    "47970268L",
    "Martí",
    "Llinés Viñals",
    "martillines@gmail.com",
    "contrasenya423",
)
usr3 = usr.Usuari(
    "47970268N",
    "Guillem",
    "Garcia Dausà",
    "gguillem@gmail.com",
    "contrasenya213",
)
usr4 = usr.Usuari(
    "53243153T", "Josep", "Martinez", "Jmartinez@gmail.com", "contrasenya44413"
)
usr5 = usr.Usuari(
    "55245351P", "Asiel", "López", "asiellopez@gmail.com", "contrasenya44414"
)

COMPROVADOR = 0

# Test 1: Comprovar que un usuari es genera correctament
print("TEST 1: GENERAR USUARI:")

print(
    "1. Tipus classe correcte:", str(type(usr1)) == "<class 'Usuari.Usuari'>"
)
print("2. NIF correcte:", usr1.NIF == "47970268L")
print("3. Nom correcte:", usr1.nom == "Guillem")
print("4. Cognoms correcte:", usr1.cognoms == "Garcia Dausà")
print("5. Correu correcte:", usr1.correu == "ggarciadausa@gmail.com")
print("6. Contrasenya correcte:", usr1.pwd == "contrasenya123")

if str(type(usr1)) == "<class 'Usuari.Usuari'>":
    COMPROVADOR += 1
if usr1.NIF == "47970268L":
    COMPROVADOR += 1
if usr1.nom == "Guillem":
    COMPROVADOR += 1
if usr1.cognoms == "Garcia Dausà":
    COMPROVADOR += 1
if usr1.correu == "ggarciadausa@gmail.com":
    COMPROVADOR += 1
if usr1.pwd == "contrasenya123":
    COMPROVADOR += 1
print("############################")

# Test 2: Es dona d'alta correctament un client
print("TEST 2: DONAR D'ALTA CORRECTAMENT:")
V1 = usr1.Donar_alta(True, "P")
V2 = usr2.Donar_alta(True, "p")
V3 = usr3.Donar_alta(True, "P")
print("1. Donar alta correctament Usr1:", V1 is True)
print("2. Donar alta incorrectament Usr2:", V2 is False)
print("3. Donar alta correctament Usr3:", V3 is True)
print("4. Diccionari registres:", usr.registres)

if V1 is True:
    COMPROVADOR += 1
if V2 is False:
    COMPROVADOR += 1
if V3 is True:
    COMPROVADOR += 1
print("############################")

# Test 3: Es genera correctament instància PersonalShopper
print("TEST 3: GENERAR CORRECTAMENT PERSONALSHOPPER:")
V4 = usr4.Donar_alta(True, "P")
print(
    "1. Comprovar data registrament:",
    usr4.data_alta == date.today().strftime("%d/%m/%Y"),
)

if usr4.data_alta == date.today().strftime("%d/%m/%Y"):
    COMPROVADOR += 1
print("############################")


# Test 4: Es genera correctament instància Client
print("TEST 4: GENERAR CORRECTAMENT CLIENT:")
V5 = usr5.Donar_alta(
    True, "C", ["645965549", "Barcelona, Granollers, Carrer Girona, 11"]
)
print(
    "1. Comprovar telefon:", usr5.telefon == "645965549"
)
print(
    "2. Comprovar adreça:",
    usr5.adress
    == "Barcelona, Granollers, Carrer Girona, 11",
)

if usr5.telefon == "645965549":
    COMPROVADOR += 1
if (
    usr5.adress
    == "Barcelona, Granollers, Carrer Girona, 11"
):
    COMPROVADOR += 1
print("############################")

# Test 5: Mètode Afegir_Metode_Pagament
print("TEST 5: MÈTODE AFEGIR_METODE_PAGAMENT")
mp1 = usr5.Afegir_Metode_Pagament(
    ["5423 2311 7187 2189", "Enric", "Gonzalez", "323", 245]
)
print(
    "1. Format correcte:",
    usr5.pagaments
    == {"5423 2311 7187 2189": ["Enric", "Gonzalez", "323", 245]},
)
mp2 = usr5.Afegir_Metode_Pagament(
    ["5423 2311 7187 2189", "Enric", "Gonzalez", "323", 245]
)
print("2. Introduir mateixa targeta:", mp2 is False)

if usr5.pagaments == {
    "5423 2311 7187 2189": ["Enric", "Gonzalez", "323", 245]
}:
    COMPROVADOR += 1
if mp2 is False:
    COMPROVADOR += 1
print("############################")

# Test 6: Mètode Esborrar_Metode_Pagament
print("TEST 6: MÈTODE ESBORRAR_METODE_PAGAMENT")
emp1 = usr5.Esborrar_Metode_Pagament(
    "5423 2311 7187 2189"
)
print("1. Esborrat correctament:", usr5.pagaments == {})
emp2 = usr5.Esborrar_Metode_Pagament(
    "5423 2311 7187 2189"
)
print("2. Esborrar targeta inexistent:", emp2 is False)

if usr5.pagaments == {}:
    COMPROVADOR += 1
if emp2 is False:
    COMPROVADOR += 1
print("############################")

# Test 7: Mètode Fer_Comanda
print("TEST 7: MÈTODE FER_COMANDA")
mp1 = usr5.Afegir_Metode_Pagament(
    ["5423 2311 7187 2189", "Enric", "Gonzalez", "323", 245]
)
mp2 = usr5.Afegir_Metode_Pagament(
    ["7223 1323 7853 5376", "Enric", "Gonzalez", "121", 7]
)

cmd1 = usr5.Fer_Comanda(True, 1)
print(
    "1. Es realitza correctament primera comanda:",
    usr5.pagaments["5423 2311 7187 2189"][-1] == 245,
)

cmd2 = usr5.Fer_Comanda(True, 2)
print("2. No es pot realitzar segona comanda:", cmd2 is False)

if usr5.pagaments["5423 2311 7187 2189"][-1] == 245:
    COMPROVADOR += 1
if cmd2 is False:
    COMPROVADOR += 1
print("############################")

# Test 8: Mètode Canviar_Personal_Shopper
print("TEST 8: MÈTODE Canviar_Personal_Shopper")
ps1 = usr5.personalShopper
usr5.Canviar_Personal_Shopper(True, "s")
ps2 = usr5.personalShopper
usr5.Canviar_Personal_Shopper(True, "n")
ps3 = usr5.personalShopper

print("1. Es canvia correctament:", ps1 != ps2)
print("2. No es canvia de Personal Shopper:", ps2 == ps3)

if ps1 != ps2:
    COMPROVADOR += 1
if ps2 == ps3:
    COMPROVADOR += 1
print("############################")

# Test 9: Mètode Assignar_Productes_Client
print("TEST 9: MÈTODE Canviar_Personal_Shopper")

pr1 = pr.Producte("0000A", "pantalons", 12, "Descripció sobre pantalons")
pr2 = pr.Producte("0000B", "jersei", 13, "Descripció sobre samarreta")
pr3 = pr.Producte("0000C", "camisa", 15, "Descripció sobre camisa")
pr4 = pr.Producte("0000D", "jaqueta", 20, "Descripció jaqueta")
pr5 = pr.Producte("0000E", "mitjons", 5, "Mitjons de ratlles")

llistat1 = [pr1, pr2, pr3]
llistat2 = [pr1, pr2, pr3, pr4, pr5]
llistat3 = [pr1, pr2, pr3, pr1, pr2, pr3]

cmp1 = usr5.personalShopper.Assignar_Productes_Client(
    usr5, llistat1
)
cmp2 = usr5.personalShopper.Assignar_Productes_Client(
    usr5, llistat3
)
cmp3 = usr5.personalShopper.Assignar_Productes_Client(
    usr5, llistat2
)
cmp4 = usr5.personalShopper.Assignar_Productes_Client(
    usr5, llistat2
)

print("1. Falta de productes:", cmp1 is False)
print("2. Productes repetits", cmp2 is False)
print("3. Es realitza correctament la assignació:", cmp3 is True)
print("4. No té pendent cap comanda:", cmp4 is False)

if not cmp1:
    COMPROVADOR += 1
if not cmp2:
    COMPROVADOR += 1
if cmp3:
    COMPROVADOR += 1
if not cmp4:
    COMPROVADOR += 1
print("############################")

# Test 10: Mètode Retornar_Producte
usr5.comandes[1] = [pr.Producte(i, "Roba", 20, "Camiseta") for i in range (5)]
usr5.Retornar_Producte(
    True, [1, 1, "Perquè no és de la meva talla"]
)
print(
    "1. Retornar producte correctament:",
    len(usr5.comandes[1]) == 4,
)

if len(usr5.comandes[1]) == 4:
    COMPROVADOR += 1
print("############################")

print("------------------------------------------------------------------")
if COMPROVADOR == 25:
    print("EVALUACIÓ DELS TEST: TOT EN FUNCIONAMENT!")
else:
    print("EVALUACIÓ DELS TEST: ALGUNA COMPROVACIÓ NO ÉS CORRECTE")
print("------------------------------------------------------------------")
