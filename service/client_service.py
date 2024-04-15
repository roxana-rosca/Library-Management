from domain.entities import Client
from domain.validators import ClientValidator
from repository.client_repo import FileRepositoryC
# InMemoryRepositoryC


class ClientService:
    """
    Responsabil de efectuarea operatiilor cerute de utilizator
    Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
    """

    def __init__(self, repoC, validatorC):
        """
        Initializeaza service
        :param repoC: obiect de tip repo care ne ajuta sa gestionam multimea de clienti
        :type repoC: InMemoryRepositoryC
        :param validatorC: validator pentru verificarea clientilor
        :type validatorC: ClientValidator
        """
        self.__repo = repoC
        self.__validator = validatorC

    def add_client(self, id, nume, cnp):
        """
        Adaugare client
        :param id: id-ul clientului
        :type id: int
        :param nume: numele clientului
        :type nume: str
        :param cnp: cnp-ul clientului
        :type cnp: int, format din exact 13 cifre
        :return: obiectul de tip Client creat
        :rtype: clientul s-a adaugat in lista
        :raises: ValueError cand clientul are date invalide
        """
        c = Client(id, nume, cnp)

        self.__validator.validate_client(c)
        self.__repo.store_client(c)
        return c

    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii existenti.
        :return: lista de clienti existenti
        :rtype: list of objects de tip Client
        """
        return self.__repo.get_all_clients()

    def delete_client(self, id):
        """
        Sterge clientul din lista cu id-ul dat.
        :param id: id-ul dat
        :return:
        :raises ValueError daca nu exista un client cu id-ul dat
        """
        return self.__repo.delete_by_id(id)

    def update_client(self, id, nume, cnp):
        c = Client(id, nume, cnp)

        self.__validator.validate_client(c)
        return self.__repo.update(id, c)


def test_add_client():
    pass
