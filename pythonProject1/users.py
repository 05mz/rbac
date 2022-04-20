#!/usr/bin/python3

# Entity Users.


class Users:


    def __init__(self):
        super().__init__()
        # initialize users
        self.users = {}

    def addUser(self, user, roles=[]):
     
        # validation of role
        for role in roles:
            assert not role or role in self.roles

        self.users.setdefault(user, set())
        self.users[user].update(roles)
