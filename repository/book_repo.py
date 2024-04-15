import io
from domain.entities import Book
from exceptions.exceptions import DuplicateIDException, BookNotFoundException


class InMemoryRepositoryB:
    """
    Clasa creata cu scopul de a gestiona multimea de carti.

    create, update, delete
    """

    def __init__(self):
        # [ book1, book2, ...]
        self.__books = []

    def find(self, id):
        """
        Cauta cartea cu id-ul dat.
        :param id: id dat
        :return: cartea cu id-ul dat, None daca nu exista
        """
        for book in self.__books:
            if book.get_id() == id:
                return book
        return None

    def store_book(self, book):
        """
        Adauga o carte in lista.
        :param book: cartea care se adauga
        :type book: Book
        :return: -; lista de carti se modifica prin adaugarea cartii date
        """
        # verificare id duplicat
        if self.find(book.get_id()) is not None:
            raise DuplicateIDException()

        self.__books.append(book)

    def get_all_books(self):
        """
        Returneaza lista cu toate cartile existente.
        :rtype: list of objects de tip Book
        """
        return self.__books

    def size(self):
        """
        Returneaza numarul de carti din multime.
        :return: numar de carti existente
        """
        return len(self.__books)

    def delete_by_id(self, id):
        """
        Sterge cartea dupa id.
        :param id: id-ul cartii care trebuie eliminata
        :return: cartea stearsa
        :raises: ValueError daca nu exista id-ul
        """
        book = self.find(id)
        if book is None:
            raise BookNotFoundException()

        self.__books.remove(book)
        return book

    def update(self, id, modified_book):
        book = self.find(id)
        if book is None:
            raise BookNotFoundException()

        return modified_book


def setup_test_repo():
    pass


def test_find():
    pass


def test_size():
    pass


def test_store_book():
    pass


def test_get_all_books():
    pass


def test_delete():
    pass


class FileRepositoryB:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        """
        try:
            f = open(self.__filename, 'r')
            # f = io.open(self.__filename, mode="r", encoding="utf-8")  # pentru diacritice
        except IOError:
            return

        lines = f.readlines()
        all_books = []
        for line in lines:
            book_id, book_title, book_author, book_description = [token.strip() for token in line.split(';')]
            book_id = int(book_id)

            b = Book(book_id, book_title, book_author, book_description)
            all_books.append(b)

        f.close()

        return all_books

    def __save_to_file(self, all_books):
        """
        Salveaza cartile in fisier.
        """
        with open(self.__filename, 'w') as f:
            for book in all_books:
                book_string = str(book.get_id()) + ";" + str(book.get_title()) + ";" + str(
                    book.get_author()) + ";" + str(book.get_description()) + '\n'
                f.write(book_string)

    def find(self, id):
        """
        Cauta cartea cu id-ul dat
        :param id: id dat
        :type id: int
        :return: cartea cu id-ul dat, None daca nu exista
        :rtype: Book
        """
        all_books = self.__load_from_file()
        for book in all_books:
            if book.get_id() == id:
                return book
        return None

    def find_recursive(self, id, all_books, n):
        # apel: find_recursive(id, all_books, len(all_books)-1)
        if n < 0:
            return None
        if all_books[n].get_id() == id:
            return all_books[n]
        else:
            return self.find_recursive(id, all_books, n - 1)

    def store_book(self, book):
        """
        Adauga o carte in lista
        :param book: cartea care se adauga
        :type book: Book
        :return: -; lista de carti se modifica prin adaugarea cartii date
        :raises: DuplicateIDException daca aceasta carte exista deja
        """
        all_books = self.__load_from_file()
        if book in all_books:
            raise DuplicateIDException()

        all_books.append(book)
        self.__save_to_file(all_books)

    def get_all_books(self):
        """
        Returneaza lista cu toate cartile existente
        :rtype: list of objects de tip Book
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de carti din multime
        :return: numar de carti existente
        :rtype: int
        """
        return len(self.__load_from_file())

    def __find_index(self, all_books, id):
        """
        Gaseste pozitia in lista a cartii cu id-ul dat
        :param all_books: lista cu toate cartile
        :type all_books: list of Book objects
        :param id: id-ul cautat
        :type id: int
        :return: pozitia in lista a cartii date, -1 daca nu exista
        :rtype: int, >=0, <repo.size()
        """
        index = -1
        for i in range(len(all_books)):
            if all_books[i].get_id() == id:
                index = i
        return index

    def find_indexx(self, id):
        all_books = self.__load_from_file()
        index = -1
        for i in range(len(all_books)):
            if all_books[i].get_id() == id:
                index = i
        return index

    def delete_by_id(self, id):
        """
        Sterge cartea dupa id.
        :param id: id-ul cartii care trebuie eliminata
        :return: cartea stearsa
        :raises: BookNotFoundException daca nu exista id-ul
        """
        all_books = self.__load_from_file()
        index = self.__find_index(all_books, id)
        if index == -1:
            raise BookNotFoundException()

        deleted_book = all_books.pop(index)

        self.__save_to_file(all_books)
        return deleted_book

    def update(self, id, modified_book):
        """
        Modifica datele cartii cu id-ul dat
        :param id: id dat
        :type id: int
        :param modified_book: cartea cu datele noi
        :type modified_book: Book
        :return: cartea modificata
        :raises: BookNotFoundException daca nu exista cartea cu id-ul dat in lista
        """
        all_books = self.__load_from_file()
        index = self.__find_index(all_books, id)
        if index == -1:
            raise BookNotFoundException()

        all_books[index] = modified_book

        self.__save_to_file(all_books)
        return modified_book

    def delete_all(self):
        self.__save_to_file([])
