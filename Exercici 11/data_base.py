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
        self.connection = sqlite3.connect(database_name)
        self.connection.execute("PRAGMA foreign_keys = ON")

    def __create_database(self):
        logging.debug("Creating Data Base if doesn't exist already.")
        self.cursor = self.connection.cursor()
        self.cursor = create_first_level_tables(cur)
        self.connection.commit()
        self.cursor = create_second_level_tables(cur)
        self.connection.commit()
        cur = database_values(cur)
        self.connection.commit()
        logging.debug("Try of inicialization finished.")
