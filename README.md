# rbac

Role Based Access Control: 
Implement a role-based authentication system. System should be able to assign a role to user and remove a user from the role. 
Entities are USER, ACTION TYPE, RESOURCE, ROLE 
ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE) 
Resource Storage: Database (PostgreSQL or Mongo) 
Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource system should be able to tell whether user has access or not. 
Note: 
· Create class-based structure using OOPS concept. 
· Follow file structure to make code maintainable and production ready. 
· Go through git commands and push the code in git with README.md. 
· This is a command line application. 
· You do not need to create functionality to add/delete/update users or any other entities. You can get it pre-created.

three tables: employee, company, salary

create these tables, and all this edit/read/delete has to happen from django.
These access controls will also be code-level, not db-level.
