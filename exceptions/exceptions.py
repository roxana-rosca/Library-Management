class BookManagerException(Exception):
    pass


class ClientManagerException(Exception):
    pass


class ValidationException(BookManagerException, ClientManagerException):
    def __init__(self, msgs):
        """
        :param msgs: lista de mesaje de eroare
        :type msgs: msgs
        """
        self.__err__msgs = msgs

    def get_messages(self):
        return self.__err__msgs

    def __str__(self):
        # return f"Validation Exception:{self.__err__msgs}"
        return "Validation Exception: " + str(self.__err__msgs)


class RepositoryException(BookManagerException, ClientManagerException):
    def __init__(self, msg):
        self.__msg = msg

    def get_message(self):
        return self.__msg

    def __str__(self):
        return "Repository Exception:" + str(self.__msg)


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID duplicat.")


class BookNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Cartea nu a fost gasita.")


class ClientNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Clientul nu a fost gasit.")


class BookAlreadyLentException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Cartea a fost deja inchiriata.")


class BookWasNotLentException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Cartea nu a fost imprumutata de catre acest client.")