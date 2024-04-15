class Book:
    def __init__(self, id, titlu, autor, descriere):
        """
        Creeaza o noua carte cu titlul, autorul si descrierea data.
        :param id:
        :param titlu:
        :param autor:
        :param descriere:
        """
        self.__id = id
        self.__title = titlu
        self.__author = autor
        self.__description = descriere

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_description(self):
        return self.__description

    def set_id(self, value):
        self.__id = value

    def set_title(self, value):
        self.__title = value

    def set_author(self, value):
        self.__author = value

    def set_description(self, value):
        self.__description = value

    def __str__(self):
        return str(
            self.__id) + ". Titlu carte: " + self.__title + '\n' + "Autor: " + self.__author + '\n' + "Descriere: " + \
               self.__description

    def __eq__(self, other):
        if self.__id == other.get_id():
            return True
        return False


class Client:
    def __init__(self, id, nume, cnp):
        """
        Creeaza un nou client cu numele si cu cnp-ul dat.
        :param id:
        :param nume:
        :param cnp:
        """
        self.__id = id
        self.__name = nume
        self.__cnp = cnp

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_cnp(self):
        return self.__cnp

    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def set_cnp(self, value):
        self.__cnp = value

    def __str__(self):
        return str(self.__id) + ".Nume client: " + self.__name + '\n' + "CNP: " + str(self.__cnp) + '\n' + "Numar de " \
                                                "carti inchiriate pana in prezent: "

    def __eq__(self, other):
        if self.__id == other.get_id():
            return True
        return False


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
"""


# tests
def test_create_book():
    book1 = Book(1, "Idiotul", "F.M. Dostoievski", "Întors la Sankt Petersburg după un lung tratament la un sanatoriu "
                                                   "din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
                                                   "înalta societatea a oraşului, care îl socoteşte sărac cu duhul.")
    assert (book1.get_title() == "Idiotul")
    assert (book1.get_author() == "F.M. Dostoievski")
    assert (book1.get_description() == "Întors la Sankt Petersburg după un lung tratament la un sanatoriu din Elveţia, "
                                       "prinţul Lev Nikolaevici Mîşkin este luat în rîs de înalta societatea a "
                                       "oraşului, "
                                       "care îl socoteşte sărac cu duhul.")

    book1.set_title("Matilda")
    book1.set_author("Roald Dahl")
    book1.set_description("Tatăl ei e un infractor, iar mama, o femeie cicălitoare şi nu tocmai inteligentă. Cei doi "
                          "cred că Matilda e o adevărată pacoste care pierde prea mult timp cu cititul în loc să se "
                          "uite la televizor, ca oamenii normali...")

    assert (book1.get_title() == "Matilda")
    assert (book1.get_author() == "Roald Dahl")
    assert (book1.get_description() == "Tatăl ei e un infractor, iar mama, o femeie cicălitoare şi nu tocmai "
                                       "inteligentă. Cei doi cred că Matilda e o adevărată pacoste care pierde prea "
                                       "mult timp cu cititul în loc să se uite la televizor, ca oamenii normali...")


def test_equals_book():
    book1 = Book(1, "Idiotul", "F.M. Dostoievski", "Întors la Sankt Petersburg după un lung tratament la un sanatoriu "
                                                   "din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
                                                   "înalta societatea a oraşului, care îl socoteşte sărac cu duhul.")
    book2 = Book(1, "Idiotul", "F. Dostoievski", "Întors la Sankt Petersburg după un lung tratament la un sanatoriu "
                                                 "din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
                                                 "înalta societatea a oraşului, care îl socoteşte sărac cu duhul.")
    assert (book1 == book2)
    book3 = Book(2, "Idiotul", "Thomas Erikson", "Întors la Sankt Petersburg după un lung tratament la un sanatoriu "
                                                 "din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
                                                 "înalta societatea a oraşului, care îl socoteşte sărac cu duhul.")
    assert (book1 != book3)


def test_create_client():
    client1 = Client(1, "Pop Andrei", 1234567891123)

    assert (client1.get_name() == "Pop Andrei")
    assert (client1.get_cnp() == 1234567891123)

    client1.set_name("Samartineanu Daniel")
    client1.set_cnp(1122334455665)

    assert (client1.get_name() == "Samartineanu Daniel")
    assert (client1.get_cnp() == 1122334455665)


def test_equals_client():
    client1 = Client(1, "Pop Andrei", 1234567891123)
    client2 = Client(1, "Pop Andrei", 1234567891123)
    assert (client1 == client2)
    client3 = Client(2, "Pop Andrei", 5534567891123)
    assert (client1 != client3)

# test_create_book()
# test_equals_book()
# test_create_client()
# test_equals_client()
