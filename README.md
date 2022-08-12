# Simple ToDo API

---
## Problem Description

**An API exists to communicate with another program. This ToDo API should allow users to create a to-do, modify an existing to-do, see the list of all to-do created, retrieve a particular todo, and delete a todo. 

The user should be able to perform the CRUD(Create-Read-Update-Delete) functionality**

### Implementation I

Follow the steps below to run this programe:

- Clone this repository on [github](https://github.com/PaulPextra/simple_todo-_api.git) to your local machine.
- Open the program folder on your code editor.
- Create a `virtual environment` and activate it.
- Install the `requirements.txt` file using the command:
`pip install -r requirements.txt`.
- Run the development server using the command:
`python manage.py runserver`.


### Implementation II

To extend this program to support a user management system where each user can access their own todos using the same endpoints, follow the steps below:

- Create a new app that extends the user model.
- Set the extended user model as the Authentication user model.
- Import and use the authentication and permission decorators on the view functions that performs the `CRUD` functionality.
- Update the view functions to take account of the logged-in user and restrict operations only to authenticated users with the right permission.

---

**Author: Paul Okoli**
[Linkedin Profile](https://www.linkedin.com/in/paulokoli/)