"Inicialitzem un diccionari contenint tots els usuaris registrats"
import datetime 
global registres 
registres = dict()

class Usuari():
    """
    Class Usuari: Es desen les dades de tota persona que es vulgui registrar a l'aplicació
    Mètodes:
        __init__: Inicialització de les instàncies
        Donar_alta: Registrar-se a l'aplicació
    """

    def __init__(self,NIF,nom,cognoms,correu,pwd):
        self.NIF = str(NIF)
        self.nom = str(nom)
        self.cognoms = str(cognoms)
        self.correu = str(correu)
        self.pwd = str(pwd)
        
    def Donar_alta(self): 
        "Retorna si s'ha donat d'alta i en cas que sigui Personal Shopper la data del registre"
        "Intentem evitar usuaris duplicats (a partir del seu NIF)"
        if self.NIF not in registres:
                        
            resposta = str(input("Vols registrar-te com a Client (C) o Personal Shopper (P)? "))
            while (resposta != "C" and resposta != "c")  and (resposta != "P" and resposta != "p"):
                resposta = str(input("Opció no vàlida, torna a seleccionar la opció (Client -> C, Personal Shopper -> P) "))
        
            if (resposta == "P") or (resposta == "p"):
                dia_actual = datetime.date.today().strftime("%d")
                classe = PersonalShopper(dia_actual, list())
            
            else:
                input_telefon = input("Posa el teu telèfon: ")
                input_adress = input("Col·loca la teva adreça física: ")
                classe = Client(input_telefon, input_adress)
            
            registres[self.NIF] = classe
            return True
        return False

class PersonalShopper(Usuari):
    """
    Class Personal Shopper: Es desen les dades de tot Personal Shopper
    Mètodes:
        __init__: Inicialització de les instàncies
    """

    def __init__(self, data_alta, clients_assignats):
        self.data_alta = data_alta
        self.clients_assignats = clients_assignats


class Client(Usuari):
    """
    Class Client: Es desen les dades de tot Client
    Mètodes:
        __init__: Inicialització de les instàncies
    """

    def __init__(self, telefon, address):
        self.telefon = telefon
        self.address = address   
        