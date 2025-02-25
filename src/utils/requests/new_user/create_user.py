from user_details import UserDetails


class CreateUser(UserDetails):

    def __init__(self, name, description, email):
        super().__init__(name, description, email)
