#!/usr/bin/python3

# Entity Roles.


class Roles:
 
    def __init__(self):
        super().__init__()
        # initialize roles
        self.roles = {}

    def addRole(self, role, actions=[]):
      
        # if not action_type provided to role
        if not actions:
            raise Exception("Invalid Action Type")

        # invalid access level
        for action in actions:
            if action.upper() not in self.action_types:
                raise Exception("Invalid Action Type")

        self.roles.setdefault(role, set())
        self.roles[role].update(actions)

    def deleteRole(self, user, role):
     
        # validation of role
        assert not role or role in self.roles

        # delete role from users
        try:
            self.users[user].remove(role)
        except KeyError:
            print("Error: No role: {0} for user: {1}".format(
                role, user))
