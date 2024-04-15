from domain.entities import Book
from domain.validators import BookValidator
from repository.book_repo import FileRepositoryB
# InMemoryRepositoryB


class BookService:
    """
    Responsabil de efectuarea operatiilor cerute de utilizator
    Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
    """

    def __init__(self, repoB, validatorB):
        """
        Initializeaza service
        :param repoB: obiect de tip repo care ne ajuta sa gestionam multimea de carti
        :type repoB: InMemoryRepositoryB
        :param validatorB: validator pentru verificarea cartilor
        :type validatorB: BookValidator
        """
        self.__repo = repoB
        self.__validator = validatorB

    def add_book(self, id, titlu, autor, descriere):
        """
        Adaugare carte
        :param id: id-ul cartii
        :type id: int
        :param titlu: tilul cartii
        :type titlu: str
        :param autor: autorul cartii
        :type: str
        :param descriere: descrierea cartii
        :type: str
        :return: obiectul de tip Book creat
        :rtype: cartea s-a adaugat in lista
        :raises: ValueError cand cartea are date invalide
        """
        b = Book(id, titlu, autor, descriere)

        self.__validator.validate_book(b)
        self.__repo.store_book(b)
        return b

    def get_all_books(self):
        """
        Returneaza o lista cu toate cartile disponibile.
        :return: lista cu cartile disponibile
        :rtype: list of objects de tip Book
        """
        return self.__repo.get_all_books()

    def delete_book(self, id):
        """
        Sterge cartea din lista cu id-ul dat.
        :param id: id-ul dat
        :return:
        :raises ValueError daca nu exista o carte cu id-ul dat
        """
        return self.__repo.delete_by_id(id)

    def update_book(self, id, titlu, autor, descriere):
        b = Book(id, titlu, autor, descriere)

        self.__validator.validate_book(b)
        return self.__repo.update(id, b)


def test_add_book():
    pass
