from domain.entities import Client
from exceptions.exceptions import ClientNotFoundException, DuplicateIDException


class InMemoryRepositoryC:
    """
    Clasa creata cu scopul de a gestiona multimea de clienti.
    """

    def __init__(self):
        # [client1, client2, ...]
        self.__clients = []

    def find(self, id):
        """
        Cauta clientul cu id-ul dat.
        :param id: id dat
        :return: clientul cu id-ul dat, None daca nu exista
        """
        for client in self.__clients:
            if client.get_id() == id:
                return client
        return None

    def store_client(self, client):
        """
        Adauga un client in lista.
        :param client: clientul care se adauga
        :type client: Client
        :return: -; lista de clienti se modifica prin adaugarea clientului dat
        """
        # verificare id duplicat
        if self.find(client.get_id()) is not None:
            raise DuplicateIDException()

        self.__clients.append(client)

    def get_all_clients(self):
        """
        Returneaza lista cu toti clientii existenti.
        :rtype: list of objects de tip Client
        """
        return self.__clients

    def size(self):
        """
        Returneaza numarul de clienti din multime.
        :return: numar de clienti existenti
        """
        return len(self.__clients)

    def delete_by_id(self, id):
        """
        Sterge clientul dupa id.
        :param id: id-ul clientului care trebuie eliminat
        :return: clientul sters
        :raises: ValueError daca nu exista id-ul
        """
        client = self.find(id)
        if client is None:
            raise ClientNotFoundException()

        self.__clients.remove(client)
        return client

    def update(self, id, modified_client):
        client = self.find(id)
        if client is None:
            raise ClientNotFoundException()

        return modified_client


def test_store_client():
    pass


def test_get_all_clients():
    pass


class FileRepositoryC:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        """
        try:
            g = open(self.__filename, 'r')
        except IOError:
            return

        lines = g.readlines()
        all_clients = []
        for line in lines:
            client_id, client_name, client_cnp = [token.strip() for token in line.split(';')]
            client_id = int(client_id)
            client_cnp = int(client_cnp)

            c = Client(client_id, client_name, client_cnp)
            all_clients.append(c)

        g.close()
        return all_clients

    def __save_to_file(self, all_clients):
        """
        Salveaza clientii in fisier
        """
        with open(self.__filename, 'w') as g:
            for client in all_clients:
                client_string = str(client.get_id()) + ";" + str(client.get_name()) + ";" + str(client.get_cnp()) + '\n'
                g.write(client_string)

    def find(self, id):
        """
        Cauta clientul cu id-ul dat
        :param id: id dat
        :type id: int
        :return: clientul cu id-ul dat, None daca nu exista
        :rtype: Client
        """
        all_clients = self.__load_from_file()
        for client in all_clients:
            if client.get_id() == id:
                return client
        return None

    def find_indexx(self, id):
        all_clients = self.__load_from_file()
        index = -1
        for i in range(len(all_clients)):
            if all_clients[i].get_id() == id:
                index = i
        return index

    def store_client(self, client):
        """
        Adauga un client in lista
        :param client: clientul care se adauga
        :type client: Client
        :return: -; lista de clienti se modifica prin adaugarea clientului dat
        :raises: DuplicateIDException daca acest client exista deja
        """
        all_clients = self.__load_from_file()
        if client in all_clients:
            raise DuplicateIDException()

        all_clients.append(client)
        self.__save_to_file(all_clients)

    def get_all_clients(self):
        """
        Reaturneaza lista cu toti clientii existenti
        :rtype: list of objects de tip Client
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de clienti din multime
        :return: numar de clienti existenti
        :rtype: int
        """
        return len(self.__load_from_file())

    def __find_index(self, all_clients, id):
        """
        Gaseste pozitia in lista a clientului cu id-ul dat
        :param all_clients: lista cu toti clientii
        :type all_clients: lista cu toti clientii
        :param id: id-ul cautat
        :type id: int
        :return: pozitia in lista a clientului dat, -1 daca nu exista
        :rtype: int, >=0, <repo.size()
        """
        index = -1
        for i in range(len(all_clients)):
            if all_clients[i].get_id() == id:
                index = i
        return index

    def delete_by_id(self, id):
        """
        Sterge clientul dupa id
        :param id: id-ul clientului care trebuie eliminat
        :return: clientul sters
        :raises: ClientNotFoundException daca nu exista id-ul
        """
        all_clients = self.__load_from_file()
        index = self.__find_index(all_clients, id)
        if index == -1:
            raise ClientNotFoundException()

        deleted_client = all_clients.pop(index)

        self.__save_to_file(all_clients)
        return deleted_client

    def update(self, id, modified_client):
        """
        Modifica datele clientului cu id-ul dat
        :param id: id dat
        :type id: int
        :param modified_client: clientul cu datele noi
        :type modified_client: Client
        :return: clientul modificat
        :raises: ClientNotFoundException daca nu exista clientul cu id-ul dat
        """
        all_clients = self.__load_from_file()
        index = self.__find_index(all_clients, id)
        if index == -1:
            raise ClientNotFoundException()

        all_clients[index] = modified_client

        self.__save_to_file(all_clients)
        return modified_client

    def delete_all(self):
        self.__save_to_file([])