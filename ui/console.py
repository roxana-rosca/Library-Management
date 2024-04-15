from domain.entities import Book, Client
import random
import string
from exceptions.exceptions import ValidationException, DuplicateIDException, BookNotFoundException, \
    ClientNotFoundException, BookAlreadyLentException, BookWasNotLentException


class Console:
    def __init__(self, book_srv, client_srv, inchiriere_srv):
        """
        Initializeaza consola.
        :param book_srv: BookService
        :param client_srv: ClientService
        """
        self.__book_service = book_srv
        self.__client_service = client_srv
        self.__inchiriere_service = inchiriere_srv
        self.__commands = {"adauga_carte": self.__add_book, "adauga_client": self.__add_client,
                           "arata_carti": self.__print_all_books, "arata_clienti": self.__print_all_clients,
                           "sterge_carte": self.__delete_book, "sterge_client": self.__delete_client,
                           "modifica_carte": self.__update_book, "modifica_client": self.__update_client,
                           "random_book": self.__add_book_random, "random_client": self.__add_client_random,
                           "inchiriere": self.__lend_book, "arata_inchirieri": self.__print_inchirieri,
                           "returnare": self.__return_book, "top_carti": self.__top_books,
                           "ordonare_clienti": self.__ordonare_clienti, "top_clienti": self.__top_clients,
                           "ordonare_inchirieri": self.__ordonare_inchirieri, "lab9": self.__client_autor}

    def __print_all_books(self):
        """
        Afiseaza toate cartile disponibile.
        """
        book_list = self.__book_service.get_all_books()
        if len(book_list) == 0:
            print("Nu exista carti in lista.")
        else:
            print("Biblioteca are o colectie de " + str(len(book_list)) + " carti.")
            print("Lista de carti este:")
            for book in book_list:
                print(book)

    def __print_all_clients(self):
        """
        Afiseaza toti clientii existenti.
        """
        client_list = self.__client_service.get_all_clients()
        if len(client_list) == 0:
            print("Nu exista clienti in lista.")
        else:
            print("Lista de clienti este:")
            for client in client_list:
                print(client)

    def __add_book_random(self):
        letters = string.ascii_lowercase
        id = random.randint(1, 100)
        titlu = ''.join(random.choice(letters) for i in range(10))
        autor = ''.join(random.choice(letters) for i in range(10))
        descriere = ''.join(random.choice(letters) for i in range(10))

        try:
            added_book = self.__book_service.add_book(id, titlu, autor, descriere)
            print("Cartea \"" + added_book.get_title() + "\", scrisa de " + added_book.get_author() + ", a fost "
                                                                                                      "adaugata cu "
                                                                                                      "succes!")
        except ValueError as ve:
            print("Cartea cu acest ID generat random a fost adaugata inainte.")

    def __add_client_random(self):
        letters = string.ascii_lowercase
        id = random.randint(1, 100)
        nume = ''.join(random.choice(letters) for i in range(10))
        cnp = random.randint(1000000000000, 9999999999999)

        try:
            added_client = self.__client_service.add_client(id, nume, cnp, )
            print("Clientul " + added_client.get_name() + ", a fost adaugat cu succes!")
        except ValueError as ve:
            print(str(ve))

    def __add_book(self):
        """
        Adauga o carte cu datele citite de la tastatura
        """
        try:
            id = int(input("Introduceti id-ul cartii:"))
        except ValueError:
            print("ID-ul trebuie sa fie un numar.")
            return
        titlu = input("Introduceti titlul cartii: ")
        autor = input("Introduceti autorul cartii: ")
        descriere = input("Introduceti descrierea cartii: ")

        try:
            added_book = self.__book_service.add_book(id, titlu, autor, descriere)
            print("Cartea \"" + added_book.get_title() + "\", scrisa de " + added_book.get_author() + ", a fost "
                                                                                                      "adaugata cu "
                                                                                                      "succes!")
        except ValidationException as ve:
            print(str(ve))
        except DuplicateIDException as e:
            print(str(e))

    def __delete_book(self):
        id = int(input("Dati ID-ul cartii pe care doriti sa o stergeti: "))
        try:
            deleted_book = self.__book_service.delete_book(id)
            print("Cartea " + deleted_book.get_title() + " a fost stearsa cu succes!")
        except BookNotFoundException as e:
            print(str(e))

    def __update_book(self):
        try:
            id = int(input("Introduceti id-ul cartii pe care doriti sa o modificati:"))
        except ValueError:
            print("ID-ul trebuie sa fie un numar.")
            return
        titlu = input("Introduceti noul titlu: ")
        autor = input("Introduceti noul autor: ")
        descriere = input("Introduceti noua descriere: ")
        try:
            modified_book = self.__book_service.update_book(id, titlu, autor, descriere)
            print("Cartea " + modified_book.get_title() + " a fost modificata cu succes!")
        except BookNotFoundException as e:
            print(str(e))
        except ValidationException as ve:
            print(str(ve))

    def __add_client(self):
        """
        Adauga un client cu datele citite de la tastatura
        """
        nume = input("Introduceti numele clientului: ")
        try:
            id = int(input("Introduceti id-ul clientului: "))
            cnp = int(input("Introduceti CNP-ul clientului: "))
        except ValueError:
            print("Valori invalide.")
            return

        try:
            added_client = self.__client_service.add_client(id, nume, cnp)
            print("Clientul " + added_client.get_name() + " a fost adaugat cu succes!")
        except ValidationException as ve:
            print(str(ve))
        except DuplicateIDException as e:
            print(str(e))

    def __delete_client(self):
        id = int(input("Dati ID-ul clientului pe care doriti sa il stergeti: "))
        try:
            deleted_client = self.__client_service.delete_client(id)
            print("Clientul " + deleted_client.get_name() + " a fost sters cu succes!")
        except ClientNotFoundException as e:
            print(str(e))

    def __update_client(self):
        try:
            id = int(input("Introduceti id-ul clientului pe care doriti sa il modificati:"))
        except ValueError:
            print("ID-ul trebuie sa fie un numar.")
            return
        nume = input("Introduceti noul nume: ")
        cnp = input("Introduceti noul CNP: ")

        try:
            modified_client = self.__client_service.update_client(id, nume, cnp)
            print("Clientul cu ID-ul " + str(id) + " a fost modificat cu succes!")
        except ClientNotFoundException as e:
            print(str(e))
        except ValidationException as ve:
            print(str(ve))

    def __print_inchirieri(self):
        """
        Afiseaza lista de inchirieri.
        """
        inchirieri_list = self.__inchiriere_service.get_all()
        if len(inchirieri_list) == 0:
            print("Nu exista inchirieri in lista.")
        else:
            print("Lista de inchirieri este: ")
            for inchiriere in inchirieri_list:
                print(inchiriere)

    def __lend_book(self):
        try:
            id_client = int(input("Introduceti ID-ul clientului: "))
            id_book = int(input("Introduceti ID-ul cartii pe care doriti sa o imprumutati: "))
        except ValueError:
            print("UI Exception: tip numeric invalid!")
            return

        try:
            inchiriere = self.__inchiriere_service.create_inchiriere(id_book, id_client)
            print("Cartea ", str(inchiriere.get_carte().get_title()),
                  " a fost inchiriata cu succes de catre clientul/a " + str(inchiriere.get_client().get_name()) + "!")
        except BookNotFoundException as ve:
            print(str(ve))
        except ClientNotFoundException as ve:
            print(str(ve))
        except BookAlreadyLentException as ve:
            print(str(ve))

    def __return_book(self):
        inchirieri_list = self.__inchiriere_service.get_all()
        if len(inchirieri_list) == 0:
            print("Nu exista inchirieri in lista.")
            return

        try:
            id_client = int(input("Introduceti ID-ul clientului: "))
            id_book = int(input("Introduceti ID-ul cartii pe care doriti sa o returnati: "))
        except ValueError:
            print("UI Exception: tip numeric invalid!")
            return

        try:
            returnare = self.__inchiriere_service.sterge_inchiriere(id_book, id_client)
            print("Cartea " + str(
                returnare.get_carte().get_title()) + " a fost returnata cu succes de catre clientul/a " + str(
                returnare.get_client().get_name()) + "!")
        except BookNotFoundException as ve:
            print(str(ve))
        except ClientNotFoundException as ve:
            print(str(ve))
        except BookWasNotLentException as ve:
            print(str(ve))

    def __top_books(self):
        """
        Cele mai inchiriate carti
        :return:
        """
        # de adaugat exceptii pentru cazul in care nu exista inchirieri
        carti = self.__inchiriere_service.cele_mai_inchiriate_carti()
        print("Cartile ordonate dupa numarul de inchirieri sunt:")
        for i in range(len(carti[0])):
            print(carti[0][i].get_title() + " a fost inchiriata de " + str(carti[1][i]) + " ori.")

    def __ordonare_clienti(self):
        """
        Clientii ordonati dupa nume.
        :return:
        """
        # clienti = self.__inchiriere_service.ordonare_clienti()
        # print("Clientii ordonati dupa numele lor si dupa numarul de carti inchiriate sunt:")
        # for i in range(len(clienti[0])):
        #    print(clienti[0][i].get_name() + " a inchiriat " + str(clienti[1][i]) + " carti pana acum.")

        clienti = self.__inchiriere_service.ordonare_clienti_merge_sort()
        for i in range(len(clienti)):
            print(str(clienti[i].get_name()))

    def __ordonare_inchirieri(self):
        """
        Ordoneaza inchirierile actuale
        :return:
        """
        # inchirieri = self.__inchiriere_service.ordonare_inchirieri()
        # print("Clientii care au carti inchiriate in acest moment sunt:")
        # for i in range(len(inchirieri[0])):
        #     print(str(inchirieri[i].get_client().get_name()) + " - " + str(inchirieri[i]) + " carti inchiriate")

        inchirieri = self.__inchiriere_service.ordonare_inchirieri_bingo_sort()
        for i in range(len(inchirieri)):
            print(str(inchirieri[i].get_client().get_name()))

    def __top_clients(self):
        """
        20% din cei mai activi clienti
        :return:
        """
        clienti = self.__inchiriere_service.top_clienti()
        lungime = len(clienti[0])
        lungime = 20 / 100 * lungime
        lungime = int(lungime)
        for i in range(lungime):
            print(clienti[0][i].get_name() + " a inchiriat " + str(clienti[1][i]) + " carti pana acum.")

    # lab9: pt fiecare client: a inchiriat x carti de la autorul y
    def __client_autor(self):
        lista = self.__inchiriere_service.lab9_cerinta()
        client_anterior = lista[0]
        autor_anterior = lista[1]
        nr_carti = 1
        print(lista)
        for i in range(2, len(lista), 2):
            if lista[i] == client_anterior:
                if autor_anterior == lista[i + 1]:
                    nr_carti += 1
                else:
                    print("Clientul " + str(client_anterior) + " a inchiriat " + str(nr_carti) + " carti scrise de " +
                          str(autor_anterior))
                    autor_anterior = lista[i + 1]
                    nr_carti = 1
            else:
                print("Clientul " + str(client_anterior) + " a inchiriat " + str(nr_carti) + " carti scrise de " + str(
                    autor_anterior))
                client_anterior = lista[i]
                autor_anterior = lista[i + 1]
                nr_carti = 1
                i -= 2
        print("Clientul " + str(client_anterior) + " a inchiriat " + str(nr_carti) + " carti scrise de " + str(
            autor_anterior))

    def run(self):
        meniu = "|".join(f"{key}" for key, value in self.__commands.items())
        while True:
            print("Comenzi disponibile: \n" + meniu + "|exit")
            comanda = input(">>> ")
            comanda = comanda.lower().strip()  # se sterg spatiile de la inceputul si de la finalul valorii introduse
            # de la tastatura
            if comanda == "":
                continue
            if comanda == "exit":
                print("Va multumim ca ati vizitat biblioteca nostra!\nLa revedere!")
                return
            if comanda in self.__commands:
                try:
                    self.__commands[comanda]()
                except ValueError:
                    print("UI Exception: tip numeric invalid!")
                except ValidationException as ve:
                    print(f"Validation Exception:{ve}")
            else:
                print("Comanda invalida! Reincercati!")
