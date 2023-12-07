"Inicialitzem un diccionari contenint tots els usuaris registrats"
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
        "Intentem evitar usuaris duplicats (a partir del seu NIF)"
        if self.NIF not in registres:
            #llista_dades = [self.nom, self.cognoms, self.correu, self.pwd]
            registres[self.NIF] = self
            return True
        return False