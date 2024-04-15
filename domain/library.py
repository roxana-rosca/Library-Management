# dtos
"""
class Library:
    def __init__(self, nume_client, titlu_carte):
        self.__nume_client = nume_client
        self.__titlu_carte = titlu_carte

    def get_nume_client(self):
        return self.__nume_client

    def get_titlu_carte(self):
        return self.__titlu_carte

    def set_nume_client(self, value):
        self.__nume_client = value

    def set_titlu_carte(self, value):
        self.__titlu_carte = value




class LibraryInfo:
    def __init__(self, titlu_carte, inchirieri_initiale):
        self.__titlu_carte = titlu_carte
        self.__total_inchirieri = inchirieri_initiale  # eventual 0

    def get_titlu_carte(self):
        return self.__titlu_carte

    def get_nr_inchirieri(self):
        return self.__total_inchirieri

    def increare_nr_inchirieri(self):
        self.__total_inchirieri += 1
"""


class Inchiriere:
    def __init__(self, carte, client):
        self.__carte = carte  # entitate de tip carte (id,titlu,autor descriere)
        self.__client = client  # entitate de tip client (id,nume,cnp)

    def get_carte(self):
        return self.__carte

    def get_client(self):
        return self.__client

    def set_carte(self, value):
        self.__carte = value

    def set_client(self, value):
        self.__client = value

    def __str__(self):
        return "Carte: " + str(self.__carte.get_title()) + " ( " + str(
            self.__carte.get_author()) + ", ID: " + str(self.__carte.get_id()) + " ) -> Client: " + str(
            self.__client.get_name()) + " ( CNP: " + str(
            self.__client.get_cnp()) + ", ID: " + str(self.__client.get_id()) + " )"

    def __eq__(self, other):
        # and self.__client == other.__client:
        if self.__carte == other.__carte:
            return True
        return False
