#!/usr/bin/env python3.9
import getpass
from pswdmanage import User
from pswdmanage import Credentials

def homepage():
    print("")
    print("     WELCOME TO PASSWORD MANAGER APPLICATION")
    print("---------------------------------------------------")
    print("    FOLLOW THE PROMPT PROCEDURES TO PROCEED  ")
    print("")
    print("        Enter username and password")
    print("")
homepage()

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user