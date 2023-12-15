from Productes import Producte
from data_base import DataBase
from Usuari import Usuari, Client, PersonalShopper

database_t = DataBase("final")

producte = Producte("codi1", "nom1", 17.34, "descripcio1")
database_t.insert_producte(producte)

usr1 = Usuari(
    "47970268L",
    "Guillem",
    "Garcia Dausà",
    "ggarciadausa@gmail.com",
    "contrasenya123",
)
database_t.insert_usuari(usr1)

usr1.Donar_alta(True, "P")
database_t.insert_personalshopper(usr1)

usr2 = Usuari(
    "76942050F",
    "Joel",
    "Tapia Salvador",
    "JTaSa@gmail.com",
    "abracadabra",
)
database_t.insert_usuari(usr2)

usr2.Donar_alta(True, "C", ["378956237", "Barcelona, St. Esteve de les Roures, Plaça Espanya, 10"])
database_t.insert_client(usr2)

