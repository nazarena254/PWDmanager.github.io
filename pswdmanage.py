#import all the python modules needed in our classes
import pyperclip
import random
import string

# first class to create user login account
class User:
    """
    User class will generates new object/instances of User.
    """
    user_list = [] # new users will be appended in this list

    def __init__(self, username, password):
        """
        This method defines the properties needed when instanciating a new User.
        """
        # self.username = username.capitalize()
        self.username = username
        self.password = password

    def save_user(self):
        """
        This method will saves a new user and append to the user list
        """
        User.user_list.append(self)
    
    @classmethod
    def display_user(cls):
        return cls.user_list
    def delete_user(self):
        '''
        This method uses .remove() mthd to delete an already saved account from the user_list
        '''
        User.user_list.remove(self)
    def user_detail(self):
        print(self.username)
        print(self.password)

def main(): #This function will not be called when other modules are ran
    new_user = User (username="annet",password="annet254") 
    new_user.user_detail() 

if __name__=="__main__": #only up one running this file will the line 38-40 be executed
    main() 

# second class to handle users credential accounts
class Credentials():
    """
    Credentials class will generates new object/instances of Credentials
    """
    credentials_list = [] #list to append users crediantial accounts
    @classmethod
    def validate_user(cls,username, password):
        """
        This method to validate whether the user is in our user_list or not.
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self, account, userName, password):
        """
         This method defines the properties needed when instanciating new account Credentials.
        """
        self.account = account
        self.userName = userName
        self.password = password    
    def save_details(self):
        """
        This method appends new account credential to the credentials_list.
        """
        Credentials.credentials_list.append(self) 
    @classmethod
    def search_credential(cls, account):
        """
        This method takes account_name as parameter and returns a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    def delete_credentials(self):
        """
        This method uses .remove() mthd to delete one account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)            
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        This method confirms if a credential exists from the credential list
         and returns True or False depending on credential existence.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """
        This method returns all list items(credential accounts) in the credentials list
        """
        return cls.credentials_list

    def generatePassword(stringLength=8):
        """This method will generate random password with letters,
            digits and special char list symbols"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))




