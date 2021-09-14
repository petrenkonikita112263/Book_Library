# Book Rating Django Web Project

This is the repository contains the Django Project - Book Rating. This app
for adding, viewing, and managing book reviews. 
It contains all the supporting project files necessary to run 
Django on server and to start app.

## Prerequisite

To get started with the project files, you'll need to:
1. Install [Python](https://www.python.org/downloads/)
2. Install [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone)
3. Install [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

## Usage Guide

1. Open a Terminal and run the following command `python manage.py runserver`
2. Open up a web browser and go to http://127.0.0.1:8000/
3. On the main|home page application will display the number of books in database (by this time - 18)
4. Click on Book Review Page in navbar or go to http://127.0.0.1:8000/books to see all the books with information about them
5. On Book Review Page click blue button Review to select the book and to see review information about it ratings:
   - _NOTE_ only first Book have reviews, for others there's red text information, so it soon may be added.
6. Open this page http://127.0.0.1:8000/book_search if you want to find a book by its title or contributor's name:
   - the limitation for book's title is it can be less than 3 characters, same thing for first or last name of contributor
   - the searching isn't case-sensitive
   - if there's no book the text _Nothing was found_ will be placed on page
   - the title of page will be _Search Results for_ .... if the form is filled otherwise the title will be _Book Search_.


## Administration
To access Django Admin staff of this application go to http://127.0.0.1:8000/admin.
Admin username **bookradmin** and password **_[ryb;ysq-vfufpby]**.

## Testing
At the time, users can log in and visit the website. But only user group **Help Desk User**
have these permissions:
   - Can view log entry
   - Can view permission
   - Can change user
   - Can view user

Only user Carol is in this group. To log in as user, use this info table

| Username      | Password |
| ----------- | ----------- |
| alice      | -N9H;w&K       |
| bob   | \6J>J**S        |
| carol | *_ydyY8L |
