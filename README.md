# Book Rating Django Web Project

This is the repository contains the Django Project - Book Rating. This app for adding, viewing, and managing book
reviews. It contains all the supporting project files necessary to run Django on server and to start app.

## Prerequisite

To get started with the project files, you'll need to:

1. Install [Python](https://www.python.org/downloads/)
2. Install [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone)
3. Install [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

## Usage Guide

1. Open a Terminal and run the following command `python manage.py runserver`
2. Open up a web browser and go to http://127.0.0.1:8000/
3. On the main|home page application will display the number of books in database (by this time - 18)
4. Click on Book Review Page in navbar or go to http://127.0.0.1:8000/books to see all the books with information about
   them
5. On Book Review Page click blue button Review to select the book and to see review information about it ratings:
    - _NOTE_ only first Book have reviews, for others there's red text information, so it soon may be added.
6. Open this page http://127.0.0.1:8000/book_search if you want to find a book by its title or contributor's name:
    - the limitation for book's title is it can be less than 3 characters, same thing for first or last name of
      contributor
    - the searching isn't case-sensitive
    - if there's no book the text _Nothing was found_ will be placed on page
    - the title of page will be _Search Results for_ .... if the form is filled otherwise the title will be _Book
      Search_.
7. The visitor can upload the cover image of the book and even the sample (or whole book if the visitor wants :) ). For
   this action open new page http://127.0.0.1:8000/books/2/media/ where is 2 is the number of book, or follow this
   steps:
    - run the application if it's not running
    - use the link from Usage Guide in #4
    - hit the Review button to see details about book and with button 'Add Review' there's new one 'Add Media' press it
    - you'll get the upload form: first field upload the image file (cover); last one - the document (it can be PDF,
      EPUB or other format)
    - browse these two files in your workplace and press 'Save', the successful message will be printed or error if
      there's something wrong
    - go back to http://127.0.0.1:8000/books and select the book for which you've uploaded two new files, and you'll see
      the cover of the book and the download link for sample The uploaded files will be saved in two media folder in
      root director for image file _media/book_covers/_ and for documents
      _media/book_samples/_. You can verify it go to url http://127.0.0.1:8000/media/book_covers/[your_image_name].
8. API urls:
    - to get number of books as JSON response use this link http://127.0.0.1:8000/api/first_api_view/
    - for other APIs you need a token , so first go to http://0.0.0.0:8000/api/login and send this info:
      `{"username": "[real_username]", "password": "[real_password]"}`
    - To pass the Authorization token (obtained in step 7) as a header, you can use the following command (Windows users
      can replace curl with curl.exe):
      `curl -X GET http://127.0.0.1:8000/api/books/ -H "Authorization: Token your_token"`
    - http://127.0.0.1:8000/api/books/ print JSON with details to every book, for
      specific http://127.0.0.1:8000/api/books/1/
    - to display all contributors http://127.0.0.1:8000/api/contributors/ or all
      reviews http://127.0.0.1:8000/api/reviews/ to get specific same thing as with books.

## Administration

To access Django Admin staff of this application go to http://127.0.0.1:8000/admin. Admin username and password display
in the table.

| bookradmin      | _[ryb;ysq-vfufpby] |
| ----------- | ----------- |

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
