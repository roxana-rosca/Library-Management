import unittest

from domain.entities import Client
from domain.validators import ClientValidator
from exceptions.exceptions import ValidationException


class TestCaseClientDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = ClientValidator()

    def test_create_client(self):
        client1 = Client(1, "Mihai", 1910724101677)
        self.assertEqual(client1.get_id(), 1)
        self.assertEqual(client1.get_name(), "Mihai")
        self.assertEqual(client1.get_cnp(), 1910724101677)

        client1.set_id(20)
        client1.set_name("Ana")
        client1.set_cnp(6000615178483)

        self.assertEqual(client1.get_id(), 20)
        self.assertEqual(client1.get_name(), "Ana")
        self.assertEqual(client1.get_cnp(), 6000615178483)

    def test_equals_client(self):
        client1 = Client(1, "Mihai", 1910724101677)
        client2 = Client(1, "Mihai", 1910724101677)

        self.assertEqual(client1, client2)

        client3 = Client(2, "Ana", 6000615178483)
        self.assertNotEqual(client1, client3)

    def test_client_validator(self):
        pass
