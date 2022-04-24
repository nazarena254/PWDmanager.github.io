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
def save_user(user): #save new user
    user.save_user()
def display_user(): #display user
    return User.display_user()
def login_user(username,password): #check user existence
    check_user = Credentials.validate_user(username,password)
    return check_user
def create_new_credential(account,userName,password): #create credential account for new user
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials): #append credential account to credentials_list
    credentials. save_details()
def display_accounts_details():#display saved credential accounts
    return Credentials.display_credentials()
def delete_credential(credentials):#delete a credentials account from credentials_list
    credentials.delete_credentials()
def search_credential(account): #search a credentials account details by an account name
    return Credentials.find_credential(account)
def check_credentials(account):#check if a credentials account exists with that account name and return true or false
    return Credentials.if_credential_exist(account)
def generate_Password():#generate password for a credential account
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):#copies the password taking account as parameter and using pyperclip framework
    return Credentials.copy_password(account) 

def pwdManager():
    print("")
    print("*** LETS GET STARTED ****")
    print("Enter su  to  Sign Up")
    print("OR")
    print("Enter li to Login")









