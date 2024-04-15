from domain.entities import Book, Client
from domain.library import Inchiriere
from exceptions.exceptions import BookAlreadyLentException, BookNotFoundException


class LibraryInMemoryRepo:
    def __init__(self):
        self.__inchirieri = []

    def find(self, book):
        """
        Cauta cartea in lista de inchirieri.
        :param book: cartea cautata
        :type book: Inchiriere
        :return: cartea cautata daca exista in lista, None in caz contrar
        :rtype:
        """
        for b in self.__inchirieri:
            if b == book:
                return book
        return None

    def store(self, book):
        """
        Adauga o carte in lista de carti inchiriate.
        :param book: cartea de adaugat
        :type book:
        :return: -; se adauga cartea la lista de inchirieri
        :raises: BookAlreadyLentException daca aceasta carte a fost deja inchiriata
        """
        b = self.find(book)
        if b is not None:
            raise BookAlreadyLentException()
        self.__inchirieri.append(book)

    def get_all(self):
        """
        Returneaza lista cu toate inchirierile.
        :return: lista cu cartile inchiriate
        :rtype: list of  objects
        """
        return self.__inchirieri

    def __find_index(self, inchiriere):
        """
        !!!schimba Gaseste pozitia pe care se afla cartea book in lista de carti inchiriate, -1 in caz contrar.
        :param all_inchirieri:
        :param book:
        :return:
        """
        index = -1
        i = 0
        for b in self.__inchirieri:
            if b == inchiriere:
                index = i
            i += 1
        return index

    def delete(self, inchiriere):
        """
        Sterge cartea din lista de carti inchiriate (practic, cartea este returnata)
        :param book:
        :return:
        """
        index = self.__find_index(inchiriere)
        if index == -1:
            raise BookNotFoundException()

        returned_book = self.__inchirieri.pop(index)

        return returned_book
