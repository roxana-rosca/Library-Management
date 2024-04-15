from domain.validators import BookValidator, ClientValidator
from repository.book_repo import FileRepositoryB  # , InMemoryRepositoryB
from repository.client_repo import FileRepositoryC  # InMemoryRepositoryC
from repository.library_repo import LibraryInMemoryRepo
from service.book_service import BookService
from service.client_service import ClientService
from service.library_service import LibraryService
from ui.console import Console

# repoBooks = InMemoryRepositoryB()
repo_file_book = FileRepositoryB('data/books.txt')

# repoClients = InMemoryRepositoryC()
repo_file_client = FileRepositoryC('data/clients.txt')

repo_inchirieri = LibraryInMemoryRepo()

validatorB = BookValidator()
validatorC = ClientValidator()

# srvBooks = BookService(repoBooks, validatorB)
srvBooks = BookService(repo_file_book, validatorB)

# srvClients = ClientService(repoClients, validatorC)
srvClients = ClientService(repo_file_client, validatorC)

srvInchirieri = LibraryService(repo_inchirieri, repo_file_book, repo_file_client)

ui = Console(srvBooks, srvClients, srvInchirieri)
ui.run()
