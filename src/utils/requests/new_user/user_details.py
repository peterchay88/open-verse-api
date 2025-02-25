from abc import ABC


class UserDetails(ABC):

    def __init__(self, name, description, email):
        self.name = name
        self.description = description
        self.email = email
