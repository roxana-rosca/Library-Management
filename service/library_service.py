from exceptions.exceptions import BookNotFoundException, ClientNotFoundException, BookAlreadyLentException, \
    BookWasNotLentException
from domain.library import Inchiriere
from repository.book_repo import FileRepositoryB
from repository.client_repo import FileRepositoryC
from repository.library_repo import LibraryInMemoryRepo
from service.merge_sort_with_key import merge_sort_with_key
from service.bingo_sort import bingo_sort


class LibraryService:
    def __init__(self, library_repo, book_repo, client_repo):
        self.__library_repo = library_repo
        self.__book_repo = book_repo
        self.__client_repo = client_repo

        self.__nr_carti = book_repo.size()
        self.__nr_clienti = client_repo.size()
        self.__inchirieri_per_carte = [0] * self.__nr_carti
        self.__inchirieri_per_client = [0] * self.__nr_clienti
        self.__inchirieri_curente_per_client = [0] * self.__nr_clienti

    def create_inchiriere(self, book_id, client_id):
        """
        Creeaza o inchiriere.
        :param book_id: parametrul cartii care va fi inchiriata
        :type book_id: int
        :param client_id: clientul care doreste sa inchirieze o carte
        :type client_id: int
        :return: inchirierea creata cu datele date
        :rtype: Library
        :raises: ClientNotFoundException
        """
        book = self.__book_repo.find(book_id)
        if book is None:
            raise BookNotFoundException()

        client = self.__client_repo.find(client_id)
        if client is None:
            raise ClientNotFoundException()

        inchiriere = Inchiriere(book, client)
        self.__library_repo.store(inchiriere)

        # incrementez nr de inchirieri ale cartii
        # merge doar pt cele din fisier - de adaugat si la Repo-ul initial fct de find_indexx
        poz_carte = self.__book_repo.find_indexx(book_id)
        self.__inchirieri_per_carte[poz_carte] += 1

        poz_client = self.__client_repo.find_indexx(client_id)
        self.__inchirieri_per_client[poz_client] += 1

        self.__inchirieri_curente_per_client[poz_client] += 1
        return inchiriere

    def sterge_inchiriere(self, book_id, client_id):
        book = self.__book_repo.find(book_id)  # cartea
        if book is None:
            raise BookNotFoundException()

        client = self.__client_repo.find(client_id)  # clientul
        if client is None:
            raise ClientNotFoundException()

        inchiriere = Inchiriere(book, client)
        if inchiriere is None:
            raise BookWasNotLentException()

        poz_client = self.__client_repo.find_indexx(client_id)
        self.__inchirieri_curente_per_client[poz_client] -= 1

        return self.__library_repo.delete(inchiriere)

    def get_all(self):
        return self.__library_repo.get_all()

    def cele_mai_inchiriate_carti(self):
        """
        Ordonare carti dupa numarul de inchirieri
        :return:
        """
        carti = self.__book_repo.get_all_books()
        i_carti = self.__inchirieri_per_carte  # vector de frecventa pentru nr de inchirieri/ carte
        for i in range(len(i_carti) - 1):
            for j in range(i + 1, len(i_carti)):
                if i_carti[i] < i_carti[j]:
                    aux = i_carti[i]
                    i_carti[i] = i_carti[j]
                    i_carti[j] = aux
                    # interschimbare si pentru carti
                    aux = carti[i]
                    carti[i] = carti[j]
                    carti[j] = aux
        return carti, i_carti

    def ordonare_clienti(self):
        """
        Ordonare clienti dupa nume.
        :return:
        """
        clienti = self.__client_repo.get_all_clients()
        i_inchirieri = self.__inchirieri_per_client  # vector de frecvenat pentru nr inchirieri/ client
        for i in range(len(i_inchirieri) - 1):
            for j in range(i + 1, len(i_inchirieri)):
                if clienti[i].get_name() > clienti[j].get_name():
                    aux = i_inchirieri[i]
                    i_inchirieri[i] = i_inchirieri[j]
                    i_inchirieri[j] = aux
                    # interschimbare si pentru frecventa inchirierilor
                    aux = clienti[i]
                    clienti[i] = clienti[j]
                    clienti[j] = aux
        return clienti, i_inchirieri

    def top_clienti(self):
        """
        Cei mai activi clienti.
        :return:
        """
        clienti = self.__client_repo.get_all_clients()
        i_inchirieri = self.__inchirieri_per_client  # vector de frecvenat pentru nr inchirieri/ client
        for i in range(len(i_inchirieri) - 1):
            for j in range(i + 1, len(i_inchirieri)):
                if i_inchirieri[i] < i_inchirieri[j]:
                    aux = i_inchirieri[i]
                    i_inchirieri[i] = i_inchirieri[j]
                    i_inchirieri[j] = aux
                    # interschimbare si pentru frecventa inchirierilor
                    aux = clienti[i]
                    clienti[i] = clienti[j]
                    clienti[j] = aux
        return clienti, i_inchirieri

    def ordonare_inchirieri(self):
        inchirieri = self.__library_repo.get_all()
        for i in range(len(inchirieri) - 1):
            for j in range(i + 1, len(inchirieri)):
                if inchirieri[i].get_client().get_name() > inchirieri[j].get_client().get_name():
                    aux = inchirieri[i]
                    inchirieri[i] = inchirieri[j]
                    inchirieri[j] = aux

        # unii clienti se pot repeta, ii sterg pe cei duplicati
        for i in range(len(inchirieri) - 1):
            if inchirieri[i].get_client().get_name() == inchirieri[i + 1].get_client().get_name():
                inchirieri.pop(i)
                i -= 1
        return inchirieri, self.__inchirieri_curente_per_client

    def lab9_cerinta(self):
        inchirieri = self.__library_repo.get_all()
        l = []
        for i in range(len(inchirieri)):
            l.append(inchirieri[i].get_client().get_name())
            l.append(inchirieri[i].get_carte().get_author())
        # sortare dupa elementele de pe poz pare
        for i in range(0, len(l) - 2, 2):
            for j in range(i + 2, len(l), 2):
                if l[i] > l[j]:
                    aux = l[i]
                    l[i] = l[j]
                    l[j] = aux
                    # interschimb si autorii
                    aux = l[i + 1]
                    l[i + 1] = l[j + 1]
                    l[j + 1] = aux
        return l

    def ordonare_clienti_merge_sort(self):
        """
        Ordonare clienti dupa nume.
        :return:
        """
        clienti = self.__client_repo.get_all_clients()
        sorted_clients = merge_sort_with_key(clienti, lambda x: x.get_name())
        return sorted_clients

    def ordonare_inchirieri_bingo_sort(self):
        inchirieri = self.__library_repo.get_all()
        sorted_inchirieri = bingo_sort(inchirieri, lambda x: x.get_client().get_name())

        # unii clienti se pot repeta, ii sterg pe cei duplicati
        for i in range(len(inchirieri) - 1):
            if inchirieri[i].get_client().get_name() == inchirieri[i + 1].get_client().get_name():
                inchirieri.pop(i)
                i -= 1
        return sorted_inchirieri
