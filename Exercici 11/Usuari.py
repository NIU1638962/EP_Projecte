from datetime import date
import random

"Inicialitzem un diccionari contenint tots els usuaris registrats. També una llista per veure els Personal Shoppers"
global registres, personal_shoppers
registres = dict()
personal_shoppers = list()

class Usuari():
    __slots__= ('NIF', 'nom', 'cognoms', 'correu', 'pwd')
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
                personal_shoppers.append(classe)
            
            else:
                if not test:
                    input_telefon = input("Posa el teu telèfon: ")
                    input_adress = input("Col·loca la teva adreça física: ")
                else:
                    input_telefon = dades_adicionals[0]
                    input_adress = dades_adicionals[1]
                
                random.seed(123)
                my_personal_shopper = random.choice(personal_shoppers)
                classe = Client(input_telefon, input_adress, my_personal_shopper)
                my_personal_shopper.clients_assignats.append(classe)

            registres[self.NIF] = classe
            return True
        return False

class PersonalShopper(Usuari):
    __slots__= ('data_alta', 'clients_assignats')
    """
    Class Personal Shopper: Es desen les dades de tot Personal Shopper
    Mètodes:
        __init__: Inicialització de les instàncies
        Consultar_Clients: Veure quins clients té a disposició
        Assignar_Productes_Client: Fer una selecció de productes per recomenar-li al client.
    """

    def __init__(self, data_alta, clients_assignats):
        self.data_alta = data_alta
        self.clients_assignats = clients_assignats
    
    def Consultar_Clients(self):
        print("CLIENTS ASSIGNATS:")
        print("==============================")
        for index,client in enumerate(self.clients_assignats):
            print(str(index+1) + ". " + str(client.NIF) + " - " + str(client.nom) + " " + str(client.cognoms))
    
    def Assignar_Productes_Client(self, client, productes):
        #Comprovem que el client ha fet una comanda, on encara no l'hem assignat productes
        if client.comandes[len(client.comandes)] == [] and len(set(productes)) == 5:
            client.comandes[len(client.comandes)] = productes
            return True
        return False        

class Client(Usuari):
    __slots__= ('telefon', 'adress', 'personalShopper', 'pagaments', 'comandes', 'blacklist')
    """
    Class Client: Es desen les dades de tot Client
    Mètodes:
        __init__: Inicialització de les instàncies
        Fer_Comanda: El client realitza una comanda. Com a condició s'ha de tenir un mètode de pagament amb els diners suficients per realitzar el import.
        Afegir_Metode_Pagament: S'ha d'entrar un llistat de l'informació de la targeta [IDENTIFICADOR, NOM, COGNOM, DATA_CADUCITAT, CVC, DINERS] i guardar-ho internament. 
        Esborrar_Metode_Pagament: Esborrar la targeta a partir de tenir el seu IDENTIFICADOR
        Retornar_Producte: Devolució d'un producte d'una comanda.
        Canviar_PersonalShopper: Mètode per canviar el PersonalShopper assignat. De manera permanent no es podran assignar-te els anteriors.
    """

    def __init__(self, telefon, adress, personalShopper):
        self.telefon = telefon
        self.adress = adress   
        self.personalShopper = personalShopper
        self.pagaments = dict()
        self.comandes = dict()
        self.blacklist = list()

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
        
    def Retornar_Producte(self, test=False, input_usuari_test=None):
        "Seleccionar una comanda"
        diccionari_temporal1 = dict()
        print("Selecciona una de les comandes realitzades:")
        print("==================================")
        for index,comanda in enumerate(self.comandes):
            print(str(index+1) + ". Comanda " + str(comanda))
            diccionari_temporal1[index+1] = comanda
        
        if not test:
            print()
            input_usuari = int(input("Selecciona una opció del 1 al " + str(len(self.comandes)) + ": "))
            while input_usuari < 1 and input_usuari > len(self.comandes):
                input_usuari = int(input("Torna a seleccionar una opció del 1 al " + str(len(self.comandes)) + ": "))

        else:
            print("Comanda seleccionada:", input_usuari_test[0])
            input_usuari = input_usuari_test[0]
            
        print()
        comanda = self.comandes[input_usuari]
    
        "Seleccionar producte"
        diccionari_temporal2 = dict()
        print("Selecciona uns dels productes comprats:")
        print("==================================")
        for index,producte in enumerate(comanda):
            print(str(index+1) + ". Producte " + str(producte.codi) + " (" + str(producte.nom) + ")")
            diccionari_temporal2[index+1] = producte
        
        if not test:
            input_usuari = int(input("Selecciona una opció del 1 al " + str(len(diccionari_temporal2)) + ": "))
            while input_usuari < 1 and input_usuari > len(self.comandes):
                input_usuari = int(input("Torna a seleccionar una opció del 1 al " + str(len(diccionari_temporal2)) + ": "))

        else:
            print()
            print("Producte seleccionat:", input_usuari_test[1])
            input_usuari = input_usuari_test[1]
            
        print()
        producte = comanda[input_usuari-1]
        
        "Input del motiu de devolució"
        if not test:
            motiu_devolucio = input("Descriu el per què vol retornar el producte: ")
        else:
            print("Motiu de devolució:", input_usuari_test[2])
            motiu_devolucio = input_usuari_test[2]

        "Solament es treu el producte de la comanda (No es retorna els diners fins que es retorni correctament la peaç)"
        self.comandes[input_usuari].remove(producte)

    def Canviar_Personal_Shopper(self, test = False, input_test = None):
        if not test:
            input_usuari = input("Segur que vol canviar de Personal Shopper (s/n)? ")
            while (input_usuari != 's' and input_usuari != 'S') and (input_usuari != 'n' and input_usuari != 'N'):
                input_usuari = input("Segur que vol canviar de Personal Shopper (s/n)? ")    
        else:
            input_usuari = input_test

        if (input_usuari == 's') or (input_usuari == 'S'):
            self.blacklist.append(self.personalShopper)
            new_personalShopper = self.personalShopper
            while new_personalShopper in self.blacklist:
                new_personalShopper = random.choice(personal_shoppers)
            self.personalShopper = new_personalShopper
            