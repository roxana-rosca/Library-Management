import random
from domain.entities import Book, Client
from domain.validators import BookValidator, ClientValidator
from repository.book_repo import InMemoryRepositoryB
from repository.client_repo import InMemoryRepositoryC
from service.book_service import BookService
from service.client_service import ClientService
from ui.console import Console

books = [
    [1, "Idiotul", "Feodor Dostoievski",
     "Roman în patru părţi. Întors la Sankt Petersburg după un lung tratament la un "
     "sanatoriu din Elveţia, prinţul Lev Nikolaevici Mîşkin este luat în rîs de "
     "înalta societatea a oraşului, care îl socoteşte sărac cu duhul. "],
    [2, "Acolo unde canta racii", "Delia Owens", "Zvonurile despre Fata Mlaștinii au circulat mulți ani în Barkley "
                                                 "Cove, un orășel liniștit de pe coasta Carolinei de Nord."],
    [3, "Sticletele", "Donna Tartt", "Theo Decker, un adolescent de treisprezece ani din New York, supravietuieste ca "
                                     "prin minune unei explozii care ii omoara mama intr-un muzeu de arta si intra "
                                     "fara "
                                     "voia lui in posesia unui mic tablou fascinant, preferatul mamei sale."],
    [4, "Arta subtila a nepasarii", "Mark Zusak", "O metodă nonconformistă pentru o viață mai bună"],
    [5, "We were liars",
     "E.Lockhart",
     "A rich, "
     "stunning "
     "summer "
     "mystery with a "
     "sharp twist that "
     "will leave you "
     "dying to talk "
     "about the book "
     "with a pal or "
     "ten."]]
clients = [[1, "Sabau Iasmina", 1111111111111], [2, "Rotaru Robert", 5555555555555], [3, "Rosca Roxana", 6666666666666]]
value = 3
l = random.choices(books, k=value)
c = random.choices(clients, k=2)
repoBooks = InMemoryRepositoryB()
repoClients = InMemoryRepositoryC()

validatorB = BookValidator()
validatorC = ClientValidator()

srvBooks = BookService(repoBooks, validatorB)
for book in l:
    srvBooks.add_book(book[0], book[1], book[2], book[3])

# book_list = srvBooks.get_all_books()
# for book in book_list:
#    print(book)

srvClients = ClientService(repoClients, validatorC)
for client in c:
    srvClients.add_client(client[0], client[1], client[2])

ui = Console(srvBooks, srvClients)
ui.run()
