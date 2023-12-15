# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 02:45:02 2023

@author: Joel Tapia Salvador
"""
import logging
import sqlite3

logging.basicConfig(
    filename="logging_database.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s |%(pathname)s |%(funcName)s |%(lineno)d | %(message)s",
)


class DataBase:
    def __init__(self, database_name: str):
        logging.debug("Inicializating database.")

        self.__connection = sqlite3.connect(database_name + ".db")
        self.__connection.execute("PRAGMA foreign_keys = ON")
        self.__create_database()

    def __create_database(self):
        logging.debug("Creating Data Base if doesn't exist already.")

        self.__cursor = self.__connection.cursor()

        self.__create_first_level_tables()
        self.__create_second_level_tables()
        self.__create_third_level_tables()
        self.__create_fourth_level_tables()

        logging.debug("Try of inicialization finished.")

    def __create_first_level_tables(self):
        logging.debug("Creating First Level Tables if doesn't exist already.")

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Usuaris(
                NIF TEXT PRIMARY KEY ASC NOT NULL,
                Nom  TEXT NOT NULL,
                Cognoms TEXT NOT NULL,
                Correu TEXT NOT NULL,
                Contrasenya TEXT NOT NULL
            );
            """
        )

        self.__connection.commit()

    def __create_second_level_tables(self):
        logging.debug("Creating Second Level Tables if doesn't exist already.")

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Clients(
                ClientNIF TEXT NOT NULL,
                Telefon INTEGER NOT NULL,
                AdreçaPostal TEXT NOT NULL,
                PersonalShopper TEXT NOT NULL,
                FOREIGN KEY (ClientNIF) REFERENCES Usuaris(NIF),
                FOREIGN KEY (PersonalShopper) REFERENCES Usuaris(NIF),
                PRIMARY KEY (ClientNIF)
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS PersonalShoppers(
                PShopperNIF TEXT NOT NULL,
                DataAlta INTEGER NOT NULL,
                FOREIGN KEY (PShopperNIF) REFERENCES Usuaris(NIF),
                PRIMARY KEY (PShopperNIF)
            );
            """
        )

        self.__connection.commit()

    def __create_third_level_tables(self):
        logging.debug("Creating Third Level Tables if doesn't exist already.")

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Productes(
                ProducteID TEXT PRIMARY KEY ASC NOT NULL,
                Nom TEXT NOT NULL,
                Preu REAL NOT NULL,
                Descripcio TEXT NOT NULL
            );
            """
        )

        self.__connection.commit()

    def __create_fourth_level_tables(self):
        logging.debug("Creating Fourth Level Tables if doesn't exist already.")


    def insert_usuari(self, usuari):
        usr_dict = usuari.to_dict()
        self.__cursor.execute(
            """
            INSERT INTO Usuaris(NIF, Nom, Cognoms, Correu, Contrasenya)
            VALUES(:NIF, :Nom, :Cognoms, :Correu, :Contrasenya)
            """,
            usr_dict
        )
        self.__connection.commit()

    def insert_personalshopper(self, ps):
        ps_dict = ps.to_dict()
        self.__cursor.execute(
            """
            INSERT INTO PersonalShoppers(PShopperNIF, DataAlta)
            VALUES(:PShopperNIF, :DataAlta)
            """,
            ps_dict
        )
        self.__connection.commit()

    def insert_client(self, c):
        c_dict = c.to_dict()
        self.__cursor.execute(
            """
            INSERT INTO Clients(ClientNIF, Telefon, AdreçaPostal, PersonalShopper)
            VALUES(:ClientNIF, :Telefon, :AdreçaPostal, :PersonalShopper)
            """,
            c_dict
        )
        self.__connection.commit()
    def insert_producte(self, producte):
        producte_dict = producte.to_dict()
        self.__cursor.execute(
            """
            INSERT INTO Productes(ProducteID, Nom, Preu, Descripcio)
            VALUES(:ProducteID, :Nom, :Preu, :Descripcio)
            """,
            producte_dict
        )
        self.__connection.commit()
