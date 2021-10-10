#!/usr/bin/env python3

"""
First Web Application Using Flask
"""

from flask import Flask

FLASK_APP = Flask( "My First Flask Application" )

@FLASK_APP.route( "/" )
def hello():
    """
    Functionality associated with endpoint: hello
    """
    return "Hello World!"

def main():
    """
    Main function
    """
    FLASK_APP.run( debug = True, port = 5000 )

if __name__ == "__main__":
    main()
