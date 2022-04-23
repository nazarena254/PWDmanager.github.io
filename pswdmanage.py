#import all the python modules needed in our classes
import pyperclip
import random
import string

# class to create user login account
class User:
    """
    User class will generates new object/instances of User.
    """
    user_list = [] # new users will be appended in this list

    def __init__(self, username, password):
        """
        This method defines the properties needed when instanciating a new User.
        """
        self.username = username.capitalize()
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
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)
    def user_detail(self):
        print(self.username)
        print(self.password)

def main():
    new_user = User (username="annet",password="annet254") 
    new_user.user_detail() 

if __name__=="__main__":
    main() 

   




