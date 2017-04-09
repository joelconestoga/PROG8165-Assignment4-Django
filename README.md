# PROG8165-Assignment4-Django

Create a python and django project. 
  - Create the following pages: 

1.Login
  - The the user that was registered should be able to log in.
  - The username field and the password field should not have any validation client or server side. Just a simple form that submits.(Check out django forms)

2.Logout
  - This should redirect to the login after a successful logout.

3.Registration
  - Create a new user in your database.
  - Username must allow only letters, numbers and dashes (-). It must also be at least 5 characters long.
  - The password must be at least 4 characters long.  A-z, 0-9, ^, -, _, $, /, \

4.Transaction Dashboard
  - List the transactions from the database. When a new transactions is added it will appear here.

5."Add a Transaction" Page
  - The user should be able to enter transactions. Name (A-z, 0-9, -, and spaces)
  - Use client side AND server side validation!

6."Categories" Page
  - This page should list and add additional categories. 
  - The drop-down in the Add a transaction page should be updated.
  - The entry field can allow at least 1 character which could be a-z or 0-9 and space.
