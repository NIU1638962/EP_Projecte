class Producte:
    __slots__ = ("codi", "nom", "preu", "descripcio", "valoracions")

    def __init__(self, codi, nom, preu, descripcio):
        """
        Inicialització de les instàncies de la classe Producte

        Args:
            codi (str): Codi del producte. Identificador únic
            nom (str): Nom del producte
            preu (float): Preu del producte
            descripcio (str): Característiques i descripció del producte

        Raises:
            ValueError: En cas de no poder convertir el preu que es passa en float
        """
        try:
            preu = float(preu)
        except Exception as exc:  # pylint: disable=bare-except
            raise ValueError("El valor del preu és incorrecte") from exc
        self.codi = codi
        self.nom = nom
        self.preu = preu
        self.descripcio = descripcio
        self.valoracions = []

    def __str__(self):
        return (
            "INFORMACIÓ DEL PRODUCTE\nCodi: "
            + str(self.codi)
            + "\nNom: "
            + self.nom
            + "\nPreu: "
            + str(self.preu)
            + "\nDescripció: "
            + self.descripcio
            + "\nValoracions:\n\t"
            + (
                "\n\t".join(
                    ", ".join(map(str, sublist))
                    for sublist in self.valoracions
                )
            )
        )

    def __iter__(self):
        return self.valoracions.__iter__()

    def valora(self, nom_client, NIF_client, puntuacio, opinio = ""):
        """
        Valorar un producte d'un client 

        Args:
            nom_client (str): Nom del client que ho ha valorat
            puntuacio (int): Puntuació del 0 al 6
            opinio (str): Feedback del producte. 

        Raises:
            ValueError: En cas que s'introdueixi una puntuació incorrecte.
        """
        try:
            assert puntuacio == int(puntuacio)
            assert 0 < puntuacio < 6
        except Exception as exc:  # pylint: disable=bare-except
            raise ValueError("El valor de la valoració és incorrecte") from exc
        self.valoracions.append([nom_client, NIF_client, puntuacio, opinio])

    def to_dict(self):
       return {
           "ProducteID": str(self.codi),
           "Nom": self.nom,
           "Preu": self.preu,
           "Descripcio": self.descripcio,
       }
