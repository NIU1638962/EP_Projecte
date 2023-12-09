"Inicialitzem un diccionari contenint tots els usuaris registrats"
from datetime import date
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
        
    def Donar_alta(self, test=False, tipus_usuari=None, dades_adicionals=None): 
        "Retorna si s'ha donat d'alta i en cas que sigui Personal Shopper la data del registre"
        "Intentem evitar usuaris duplicats (a partir del seu NIF)"
        if self.NIF not in registres:
            if not test:       
                resposta = str(input("Vols registrar-te com a Client (C) o Personal Shopper (P)? "))
                while (resposta != "C" and resposta != "c")  and (resposta != "P" and resposta != "p"):
                    resposta = str(input("Opció no vàlida, torna a seleccionar la opció (Client -> C, Personal Shopper -> P) "))

            else:
                resposta = tipus_usuari 

            if (resposta == "P") or (resposta == "p"):
                dia_actual = date.today().strftime("%d/%m/%Y")
                classe = PersonalShopper(dia_actual, list())
            
            else:
                if not test:
                    input_telefon = input("Posa el teu telèfon: ")
                    input_adress = input("Col·loca la teva adreça física: ")
                else:
                    input_telefon = dades_adicionals[0]
                    input_adress = dades_adicionals[1]

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
    
    def Consultar_Clients(self):
        print(self.clients_assignats)
    
    def Assignar_Productes_Cataleg(self):
        "input: Client que vols assignar"
        "Assignar els productes"
        pass

class Client(Usuari):
    """
    Class Client: Es desen les dades de tot Client
    Mètodes:
        __init__: Inicialització de les instàncies
        Fer_Comanda: El client realitza una comanda. Com a condició s'ha de tenir un mètode de pagament amb els diners suficients per realitzar el import.
        Afegir_Metode_Pagament: S'ha d'entrar un llistat de l'informació de la targeta [IDENTIFICADOR, NOM, COGNOM, DATA_CADUCITAT, CVC, DINERS] i guardar-ho internament. 
        Esborrar_Metode_Pagament: Esborrar la targeta a partir de tenir el seu IDENTIFICADOR
    """

    def __init__(self, telefon, adress):
        self.telefon = telefon
        self.adress = adress   
        self.pagaments = dict()
        self.comandes = dict()

    def Fer_Comanda(self, test = False, input_usuari_test = None):
        if self.pagaments != {}:
            diccionari_temporal = dict()
            print("Selecciona un mètode de pagament:")
            print("==================================")
            for index,pagament in enumerate(self.pagaments):
                print(str(index+1) + ". Targeta amb identificador " + str(pagament))
                diccionari_temporal[index+1] = pagament

            if not test:
                input_usuari = int(input("Selecciona una opció del 1 al " + str(len(self.pagaments)) + ": "))
                while input_usuari < 1 and input_usuari > len(self.pagaments):
                    input_usuari = int(input("Torna a seleccionar una opció del 1 al " + str(len(self.pagaments)) + ": "))

            else:
                print("Mètode seleccionat:", input_usuari_test)
                input_usuari = input_usuari_test
            
            print()
            targeta = diccionari_temporal[input_usuari]
            
            if self.comandes != {}:
                if (self.pagaments[targeta][-1] - 10) < 0:
                    print("Saldo insuficient per fer la comanda")
                    return False
                self.pagaments[targeta][-1] -= 10

            self.comandes[len(self.comandes)+1] = []
            return True
        return False


    def Afegir_Metode_Pagament(self, dades_targeta):
        if dades_targeta[0] not in self.pagaments:
            self.pagaments[dades_targeta[0]] = dades_targeta[1:]
            return True
        return False

    def Esborrar_Metode_Pagament(self, identificador):
        if identificador in self.pagaments:
            del(self.pagaments[identificador])
            return True
        return False
        
    def Retornar_Producte(self):
        "Seleccionar comanda"
        "Seleccionar producte"
        "Input del motiu"
        pass
    