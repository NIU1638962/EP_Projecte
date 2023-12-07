import Usuari as usr


print("############################")
print("TEST CLASS USUARI:")
print("############################")

usr1 = usr.Usuari("47970268L", "Guillem", "Garcia Dausà", "ggarciadausa@gmail.com", "contrasenya123")
usr2 = usr.Usuari("47970268L", "Martí", "Llinés Viñals", "martillines@gmail.com", "contrasenya423")
usr3 = usr.Usuari("47970268N", "Guillem", "Garcia Dausà", "gguillem@gmail.com", "contrasenya213")

#Test 1: Comprovar que un usuari es genera correctament
print("TEST 1: GENERAR USUARI:")
print("1. Tipus classe correcte:", str(type(usr1)) == "<class 'Usuari.Usuari'>")
print("2. NIF correcte:", usr1.NIF == "47970268L")
print("3. Nom correcte:", usr1.nom == "Guillem")
print("4. Cognoms correcte:", usr1.cognoms == "Garcia Dausà")
print("5. Correu correcte:", usr1.correu == "ggarciadausa@gmail.com")
print("6. Contrasenya correcte:", usr1.pwd == "contrasenya123")
print("############################")

#Test 2: Es dona d'alta correctament un client
print("TEST 2: DONAR D'ALTA CORRECTAMENT:")
print("1. Donar alta correctament Usr1:", usr1.Donar_alta() == True)
print("2. Donar alta incorrectament Usr2:", usr2.Donar_alta() == False)
print("3. Donar alta correctament Usr3:", usr3.Donar_alta() == True)
print("4. Diccionari registres:", usr.registres)
print("############################")




