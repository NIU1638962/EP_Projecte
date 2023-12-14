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
                UsuariID INTEGER PRIMARY KEY ASC NOT NULL,
                NIF TEXT NOT NULL,
                Nom  TEXT NOT NULL,
                Cognoms TEXT NOT NULL,
                Correu TEXT NOT NULL,
                Contrasenya TEXT NOT NULL
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Marques(
                MarcaID INTEGER PRIMARY KEY ASC NOT NULL,
                Nom TEXT NOT NULL,
                Descripció TEXT NOT NULL
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Seccions(
                SeccióID INTEGER PRIMARY KEY ASC NOT NULL,
                Nom TEXT NOT NULL,
                Descripció TEXT NOT NULL,
                ContingudaEnID INTEGER,
                FOREIGN KEY (ContingudaEnID) REFERENCES Seccions(SeccióID)
            );
            """
        )

        self.__connection.commit()

    def __create_second_level_tables(self):
        logging.debug("Creating Second Level Tables if doesn't exist already.")

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Clients(
                ClientID INTEGER NOT NULL,
                Telefon INTEGER NOT NULL,
                AdreçaPostal TEXT NOT NULL,
                FOREIGN KEY (ClientID) REFERENCES Usuaris(UsuariID),
                PRIMARY KEY (ClientID)
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Shoppers(
                ShopperID INTEGER NOT NULL,
                DataAlta INTEGER NOT NULL,
                FOREIGN KEY (ShopperID) REFERENCES Usuaris(UsuariID),
                PRIMARY KEY (ShopperID)
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Models(
                ModelID INTEGER PRIMARY KEY ASC NOT NULL,
                Nom TEXT NOT NULL,
                Descripció TEXT NOT NULL,
                MarcaID INTEGER NOT NULL,
                FOREIGN KEY (MarcaID) REFERENCES Marques(MarcaID)
            );
            """
        )

    def __create_third_level_tables(self):
        logging.debug("Creating Third Level Tables if doesn't exist already.")

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Clients_Assignats(
                ClientID INTEGER NOT NULL,
                ShopperID INTEGER NOT NULL,
                FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
                FOREIGN KEY (ShopperID) REFERENCES Shoppers(ShopperID),
                PRIMARY KEY (ClientID, ShopperID)
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Productes(
                ProducteID INTEGER PRIMARY KEY  ASC NOT NULL,
                Nom TEXT NOT NULL,
                Descripció TEXT NOT NULL,
                Preu REAL NOT NULL,
                Disponibilitat TEXT NOT NULL,
                ModelID INTEGER NOT NULL,
                FOREIGN KEY (ModelID) REFERENCES Models(ModelID)
            );
            """
        )

        self.__connection.commit()

    def __create_fourth_level_tables(self):
        logging.debug("Creating Fourth Level Tables if doesn't exist already.")

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Resenyes(
                ClientID INTEGER NOT NULL,
                ProducteID INTEGER NOT NULL,
                Puntuació INTEGER NOT NULL,
                Comentari TEXT,
                FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
                FOREIGN KEY (ProducteID) REFERENCES Productes(ProducteID),
                PRIMARY KEY (ClientID, ProducteID)
            );
            """
        )

        self.__connection.commit()

        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Pertenença(
                ProducteID INTEGER NOT NULL,
                SeccióID INTEGER NOT NULL,
                FOREIGN KEY (ProducteID) REFERENCES Productes(ProducteID),
                FOREIGN KEY (SeccióID) REFERENCES Seccions(SeccióID),
                PRIMARY KEY (ProducteID, SeccióID)
            );
            """
        )

        self.__connection.commit()

    def __add_user(self, nif: str, nom: str):
        logging.debug(f"Adding new user to databse: {nif}, {nom}, ")


database = DataBase("test")
