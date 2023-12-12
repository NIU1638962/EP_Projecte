import Usuari as usr
from datetime import date

print("############################")
print("TEST CLASS USUARI:")
print("############################")

usr1 = usr.Usuari("47970268L", "Guillem", "Garcia Dausà", "ggarciadausa@gmail.com", "contrasenya123")
usr2 = usr.Usuari("47970268L", "Martí", "Llinés Viñals", "martillines@gmail.com", "contrasenya423")
usr3 = usr.Usuari("47970268N", "Guillem", "Garcia Dausà", "gguillem@gmail.com", "contrasenya213")
usr4 = usr.Usuari("53243153T", "Josep", "Martinez", "Jmartinez@gmail.com", "contrasenya44413")
usr5 = usr.Usuari("55245351P", "Asiel", "López", "asiellopez@gmail.com", "contrasenya44414")

comprovador = 0

#Test 1: Comprovar que un usuari es genera correctament
print("TEST 1: GENERAR USUARI:")

print("1. Tipus classe correcte:", str(type(usr1)) == "<class 'Usuari.Usuari'>")
print("2. NIF correcte:", usr1.NIF == "47970268L")
print("3. Nom correcte:", usr1.nom == "Guillem")
print("4. Cognoms correcte:", usr1.cognoms == "Garcia Dausà")
print("5. Correu correcte:", usr1.correu == "ggarciadausa@gmail.com")
print("6. Contrasenya correcte:", usr1.pwd == "contrasenya123")

if str(type(usr1)) == "<class 'Usuari.Usuari'>": comprovador += 1
if usr1.NIF == "47970268L": comprovador += 1
if usr1.nom == "Guillem": comprovador += 1
if usr1.cognoms == "Garcia Dausà": comprovador += 1
if usr1.correu == "ggarciadausa@gmail.com": comprovador += 1
if usr1.pwd == "contrasenya123": comprovador += 1
print("############################")

#Test 2: Es dona d'alta correctament un client
print("TEST 2: DONAR D'ALTA CORRECTAMENT:")
v1 = usr1.Donar_alta(True, "P") 
v2 = usr2.Donar_alta(True, "p")
v3 = usr3.Donar_alta(True, "P")
print("1. Donar alta correctament Usr1:", v1 == True)
print("2. Donar alta incorrectament Usr2:", v2  == False)
print("3. Donar alta correctament Usr3:", v3 == True)
print("4. Diccionari registres:", usr.registres)

if v1 == True: comprovador += 1
if v2 == False: comprovador += 1
if v3 == True: comprovador += 1
print("############################")

#Test 3: Es genera correctament instància PersonalShopper
print("TEST 3: GENERAR CORRECTAMENT PERSONALSHOPPER:")
v4 = usr4.Donar_alta(True, "P") 
print("1. Comprovar data registrament:", usr.registres["53243153T"].data_alta == date.today().strftime("%d/%m/%Y"))

if usr.registres["53243153T"].data_alta == date.today().strftime("%d/%m/%Y"): comprovador += 1
print("############################")


#Test 4: Es genera correctament instància Client
print("TEST 4: GENERAR CORRECTAMENT CLIENT:")
v5 = usr5.Donar_alta(True, "C", ["645965549", "Barcelona, Granollers, Carrer Girona, 11"]) 
print("1. Comprovar telefon:", usr.registres["55245351P"].telefon == "645965549")
print("2. Comprovar adreça:", usr.registres["55245351P"].adress == "Barcelona, Granollers, Carrer Girona, 11")

if usr.registres["55245351P"].telefon == "645965549": comprovador += 1
if usr.registres["55245351P"].adress == "Barcelona, Granollers, Carrer Girona, 11": comprovador += 1
print("############################")

#Test 5: Mètode Afegir_Metode_Pagament
print("TEST 5: MÈTODE AFEGIR_METODE_PAGAMENT") 
mp1 = usr.registres["55245351P"].Afegir_Metode_Pagament(["5423 2311 7187 2189", "Enric", "Gonzalez", "323", 245])
print("1. Format correcte:", usr.registres["55245351P"].pagaments == {'5423 2311 7187 2189': ['Enric', 'Gonzalez', '323', 245]})
mp2 = usr.registres["55245351P"].Afegir_Metode_Pagament(["5423 2311 7187 2189", "Enric", "Gonzalez", "323", 245])
print("2. Introduir mateixa targeta:", mp2 == False)

if usr.registres["55245351P"].pagaments == {'5423 2311 7187 2189': ['Enric', 'Gonzalez', '323', 245]}: comprovador += 1
if mp2 == False: comprovador += 1
print("############################")

#Test 6: Mètode Esborrar_Metode_Pagament
print("TEST 6: MÈTODE ESBORRAR_METODE_PAGAMENT") 
emp1 = usr.registres["55245351P"].Esborrar_Metode_Pagament("5423 2311 7187 2189")
print("1. Esborrat correctament:", usr.registres["55245351P"].pagaments == {})
emp2 = usr.registres["55245351P"].Esborrar_Metode_Pagament("5423 2311 7187 2189")
print("2. Esborrar targeta inexistent:", emp2 == False)

if usr.registres["55245351P"].pagaments == {}: comprovador += 1
if emp2 == False: comprovador += 1
print("############################")

#Test 7: Mètode Fer_Comanda
print("TEST 7: MÈTODE FER_COMANDA") 
mp1 = usr.registres["55245351P"].Afegir_Metode_Pagament(["5423 2311 7187 2189", "Enric", "Gonzalez", "323", 245])
mp2 = usr.registres["55245351P"].Afegir_Metode_Pagament(["7223 1323 7853 5376", "Enric", "Gonzalez", "121", 7])

cmd1 = usr.registres["55245351P"].Fer_Comanda(True, 1)
print("1. Es realitza correctament primera comanda:", usr.registres["55245351P"].pagaments["5423 2311 7187 2189"][-1] == 245)

cmd2 = usr.registres["55245351P"].Fer_Comanda(True, 2)
print("2. No es pot realitzar segona comanda:", cmd2 == False)

if usr.registres["55245351P"].pagaments["5423 2311 7187 2189"][-1] == 245: comprovador += 1
if cmd2 == False: comprovador += 1
print("############################")

#Test 8: Mètode Canviar_Personal_Shopper
print("TEST 8: MÈTODE Canviar_Personal_Shopper") 
ps1 = usr.registres["55245351P"].personalShopper
usr.registres["55245351P"].Canviar_Personal_Shopper(True, 's')
ps2 = usr.registres["55245351P"].personalShopper
usr.registres["55245351P"].Canviar_Personal_Shopper(True, 'n')
ps3 = usr.registres["55245351P"].personalShopper

print("1. Es canvia correctament:", ps1 != ps2) 
print("2. No es canvia de Personal Shopper:", ps2 == ps3)

if ps1 != ps2: comprovador += 1
if ps2 == ps3: comprovador += 1
print("############################")

if comprovador == 20: print("EVALUACIÓ DELS TEST: TOT EN FUNCIONAMENT!")
else: print("EVALUACIÓ DELS TEST: ALGUNA COMPROVACIÓ NO ÉS CORRECTE")



