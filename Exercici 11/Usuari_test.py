import Usuari as usr


print("############################")
print("TEST CLASS USUARI:")
print("############################")

usr1 = usr.Usuari("47970268L", "Guillem", "Garcia Dausà", "ggarciadausa@gmail.com", "contrasenya123")
usr2 = usr.Usuari("47970268L", "Martí", "Llinés Viñals", "martillines@gmail.com", "contrasenya423")
usr3 = usr.Usuari("47970268N", "Guillem", "Garcia Dausà", "gguillem@gmail.com", "contrasenya213")
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
v1 = usr1.Donar_alta() 
v2 = usr2.Donar_alta()
v3 = usr3.Donar_alta()
print("1. Donar alta correctament Usr1:", v1 == True)
print("2. Donar alta incorrectament Usr2:", v2  == False)
print("3. Donar alta correctament Usr3:", v3 == True)
print("4. Diccionari registres:", usr.registres)

if v1 == True: comprovador += 1
if v2 == False: comprovador += 1
if v3 == True: comprovador += 1
print("############################")
if comprovador == 9: print("TOT EN FUNCIONAMENT!")




