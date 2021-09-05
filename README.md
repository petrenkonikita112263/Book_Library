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