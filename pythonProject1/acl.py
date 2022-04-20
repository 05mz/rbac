#!/usr/bin/python3

# Access Control List.

from rbac.action_type import ActionType


class Registry(ActionType):
   

    def __init__(self):
        super().__init__()

    def isAllowed(self, user, action_type, resource):
       

        # check whether user and resource are present or not
        assert not user or user in self.users
        assert not resource or resource in self.resources

        # get roles of user
        roles = self.users[user]

       
        if len(roles) == 1:
            role = list(roles)[0]
        if len(roles) > 1:
            # find super-set of role
            for role in roles:
                if role == 'super-admin' or role == 'admin':
                    break

   
        try:
            if self.denied[role, action_type.upper(), resource]:
                print("Error: Permission denied. User: {0} has no {1} "
                      "access to resource: {2}".format(user, action_type, resource))
                return False
        except KeyError:
            pass

        # if role not present in allowed, then return None
        try:
            if self.allowed[role, action_type.upper(), resource]:
                print("user: {0} has {1} access to "
                      "resource: {2}".format(user, action_type, resource))
                return True
        except Exception:
            print("Error: Permission denied. User: {0} has no {1} "
                  "access to resource: {2}".format(
                      user, action_type, resource))
            return None
