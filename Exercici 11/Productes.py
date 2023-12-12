class Producte():
    __slots__= ('codi', 'nom', 'preu', 'descripcio', 'valoracions')
    """
    Class Producte: representen els productes que ofereixen els proveïdors.
    Mètodes:
        __init__: inicialització dels atributs de l'instància
        Valora: Afegir una valoració al producte
    """

    def __init__(self, codi, nom, preu, descripcio):
        try:
            preu=float(preu)
        except:
            raise ValueError("El valor del preu és incorrecte")
        else:
            self.codi = codi
            self.nom = nom
            self.preu = preu
            self.descripcio = descripcio
            self.valoracions = []

    def __str__(self):
        return ("INFORMACIÓ DEL PRODUCTE\nCodi: " + str(self.codi) + "\nNom: " + self.nom + "\nPreu: " +
                str(self.preu) + "\nDescripció: " + self.descripcio + "\nValoracions:\n\t" +
                ('\n\t'.join(', '.join(map(str, sublist)) for sublist in self.valoracions)))

    def __iter__(self):
        return self.valoracions.__iter__()

    def valora(self, nom_client, puntuacio, opinio):
        try:
            assert(puntuacio==int(puntuacio))
            assert(0<puntuacio<6)
        except:
            raise ValueError("El valor de la valoració és incorrecte")
        else:
            self.valoracions.append([nom_client, puntuacio, opinio])
