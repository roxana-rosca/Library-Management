from domain.entities import Book, Client
from domain.library import Inchiriere
from exceptions.exceptions import ValidationException


class BookValidator:
    def validate_book(self, book):
        errors = []
        if book.get_id() < 0:
            errors.append("ID invalid.")
        if len(book.get_title()) <= 2:
            errors.append("Titlul trebuie sa aiba mai mult de 2 caractere.")
        if book.get_title() == "":
            errors.append("Titlul este vid.")
        if book.get_author() == "":
            errors.append("Autorul este vid.")
        if len(book.get_author()) <= 2:
            errors.append("Numele autorului trebuie sa aiba mai mult de 2 caractere.")
        if book.get_description() == "":
            errors.append("Descrierea este vida.")
        if len(book.get_description()) <= 4:
            errors.append("Descrierea este prea scurta.")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)


"""
def test_validate_book():
    test_validator = BookValidator()
    book1 = Book(1, "Idiotul", "F.M. Dostoievski", "Întors la Sankt Petersburg după un lung tratament la un sanatoriu "
                                                   "din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
                                                   "înalta societatea a oraşului, care îl socoteşte sărac cu duhul.")
    test_validator.validate_book(book1)

    book2 = Book(2, "", "Ion Creanga", "lucrare principala a autorului")
    try:
        test_validator.validate_book(book2)
        assert False
    except ValueError:
        assert True

    book3 = Book(-1, "Idiotul", "F.M. Dostoievski", "Întors la Sankt Petersburg după un lung tratament la un sanatoriu "
                                                    "din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
                                                    "înalta societatea a oraşului, care îl socoteşte sărac cu duhul.")
    try:
        test_validator.validate_book(book3)
        assert False
    except ValueError:
        assert True
"""


class ClientValidator:
    def validate_client(self, client):
        errors = []
        if client.get_id() < 0:
            errors.append("ID invalid.")
        if len(client.get_name()) < 2:
            errors.append("Numele trebuie sa aiba mai mult de 2 caractere.")
        if client.get_name() == "":
            errors.append("Numele este vid.")
        if len(str(client.get_cnp())) != 13:
            errors.append("CNP-ul trebuie sa fie format din 13 cifre.")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)


"""
def test_validate_client():
    test_validator = ClientValidator()
    client1 = Client(1, "Mara Vasiliu", 1234567891011)
    test_validator.validate_client(client1)

    client2 = Client(2, "", 1234567891011)
    try:
        test_validator.validate_client(client2)
        assert False
    except ValueError:
        assert True

    client3 = Client(3, "Mara Vasiliu", 22)
    try:
        test_validator.validate_client(client3)
        assert False
    except ValueError:
        assert True

    client4 = Client(-1, "Mara Vasiliu", 1234567891011)
    try:
        test_validator.validate_client(client4)
        assert False
    except ValueError:
        assert True


#test_validate_book()
#test_validate_client()
"""

"""
class InchiriereValidator:
    def validate(self, inchiriere):
"""

