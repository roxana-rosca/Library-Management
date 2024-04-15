import unittest

from domain.entities import Book
from domain.validators import BookValidator
from exceptions.exceptions import ValidationException


class TestCaseBookDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = BookValidator()

    def test_create_book(self):
        book1 = Book(1, "Idiotul", "F.M. Dostoievski", "Intors la Sankt Petersburg dupa un lung tratament la un "
                                                       "sanatoriu din Elvetia, printul Lev Nikolaevici Miskin este "
                                                       "luat in ris de inalta societatea a orasului, care il socoteste "
                                                       "sarac cu duhul.")
        self.assertEqual(book1.get_id(), 1)
        self.assertEqual(book1.get_title(), "Idiotul")
        self.assertEqual(book1.get_author(), "F.M. Dostoievski")
        self.assertEqual(book1.get_description(), "Intors la Sankt Petersburg dupa un lung tratament la un sanatoriu "
                                                  "din Elvetia, printul Lev Nikolaevici Miskin este luat in ris de "
                                                  "inalta societatea a orasului, care il socoteste sarac cu duhul.")
        book1.set_id(2)
        book1.set_title("Triunghiul Bermudelor")
        book1.set_author("Charles Berlitz")
        book1.set_description("Incredibila poveste a disparitiilor misterioase.")

        self.assertEqual(book1.get_id(), 2)
        self.assertEqual(book1.get_title(), "Triunghiul Bermudelor")
        self.assertEqual(book1.get_author(), "Charles Berlitz")
        self.assertEqual(book1.get_description(), "Incredibila poveste a disparitiilor misterioase.")

    def test_equals_book(self):
        book1 = Book(1, "Idiotul", "F.M. Dostoievski", "Intors la Sankt Petersburg dupa un lung tratament la un "
                                                       "sanatoriu din Elvetia, printul Lev Nikolaevici Miskin este "
                                                       "luat in ris de inalta societatea a orasului, care il socoteste "
                                                       "sarac cu duhul.")
        book2 = Book(1, "Idiotul", "F.M. Dostoievski", "Intors la Sankt Petersburg dupa un lung tratament la un "
                                                       "sanatoriu din Elvetia, printul Lev Nikolaevici Miskin este "
                                                       "luat in ris de inalta societatea a orasului, care il socoteste "
                                                       "sarac cu duhul.")
        self.assertEqual(book1, book2)

        book3 = Book(2, "Idiotul", "F.M. Dostoievski", "Intors la Sankt Petersburg dupa un lung tratament la un "
                                                       "sanatoriu din Elvetia, printul Lev Nikolaevici Miskin este "
                                                       "luat in ris de inalta societatea a orasului, care il socoteste "
                                                       "sarac cu duhul.")
        self.assertNotEqual(book1, book3)

    def test_book_validator(self):
        book1 = Book(1, "Idiotul", "F.M. Dostoievski", "Intors la Sankt Petersburg dupa un lung tratament la un "
                                                       "sanatoriu din Elvetia, printul Lev Nikolaevici Miskin este "
                                                       "luat in ris de inalta societatea a orasului, care il socoteste "
                                                       "sarac cu duhul.")
        self.__validator.validate_book(book1)
        book2 = Book(-2, "Triunghiul Bermudelor", "Charles Berlitz", "Incredibila poveste a disparitiilor misterioase.")
        book3 = Book(3, "a", "", "Incredibila poveste a disparitiilor misterioase.")

        self.assertRaises(ValidationException, self.__validator.validate_book, book2)
        self.assertRaises(ValidationException, self.__validator.validate_book, book3)
