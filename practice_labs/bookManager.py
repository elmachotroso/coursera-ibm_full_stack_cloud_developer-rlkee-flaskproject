#!/usr/bin/env python3

"""
bookManager
"""

import json
from flask import Flask, render_template

FLASK_APP = Flask( "Book Manager", static_folder = "static" )
BOOKS = []

@FLASK_APP.route( "/addBook/<bookname>/<author>" )
def add_Book ( bookname, author ):
    """
    Endpoint: add_book
    Method: GET
    Adds a book given the title and author.
    """
    BOOKS.append( { "bookname" : bookname, "author" : author } )
    return f"{ bookname } by { author } appended."

@FLASK_APP.route( "/getBooks" )
def get_books():
    """
    Endpoint: get_books
    Method: GET
    Display all known books.
    """
    return json.dumps( BOOKS )

@FLASK_APP.route( "/" )
def homepage():
    """
    Endpoint: homepage (index)
    Method: GET
    Displays the static index page.
    """
    return render_template( "index.html" )

def main():
    """
    Main function
    """
    FLASK_APP.run( debug = True, port = 5000 )

if __name__=="__main__":
    main()
