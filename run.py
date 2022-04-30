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
def find_credential(account): #search a credentials account details by an account name
    return Credentials.search_credential(account)
def check_credentials(account):#check if a credentials account exists with that account name and return true or false
    return Credentials.if_credential_exist(account)
def generate_Password():#generate password for a credential account
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):#copies the password taking account as parameter and using pyperclip framework
    return Credentials.copy_password(account) 

def main():
    print("")
    print("*** LETS GET STARTED ****")
    print("Enter su  to  Sign Up")
    print("OR")
    print("Enter li to Login")

    #.lower() converts user input to lowercase, 
    # .strip() remove the whitespace from the beginning and at the end of the string
    short_code=input("").lower().strip() 
    if short_code == "su":
        print("Continue with Sign Up")
        print("")
        username = input("Enter Username: ")
        while True:
            print("Press y to Continue ") 
            print("")          
            password_create = input().lower().strip()
            if password_create == 'y':
                print("")
                password = getpass.getpass('Enter your new PWDmanager Password: ')
                print("")
                print(username ,", your PWDamnager Password is: ", password)
                print("")
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))

    elif short_code == "li":
        print("")
        print("Enter your User name and your PWDmanager Password to log in:")
        print("")
        username = input("User name: ")
        password = getpass.getpass('Password: ')
        print("")
        login = login_user(username,password)
        if login_user == login:
            print("")
            print(username, ", Welcome to PWDmanager and store your various account passwords")  
            print("")
    while True:
        print("Enter these short codes")
        print(" nca To Create a New Credential Account \n dc To Display Credentials \n sc To Search a credential \n gp To Generate A randomn password \n del To Delete credential \n ex To Exit the application \n ")
        short_code = input().lower().strip()
        if short_code == "nca":
            print("Enter Your New Credential Account(Eg twitter) ")
            print("")
            account = input().lower()
            print("Enter Your Credential Account username")
            userName2 = input()
            while True:
                print(" tp  To type your own pasword if you already have an account")
                print("OR")
                print(" gp To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    # password = input("Enter Your Own Password")
                    password = getpass.getpass('Enter Your Own Password: ')
                    print("username ",userName2, ", Your pasword is sucessfully created")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    print("username ",userName2, ", Your pasword: ",password,"is sucessfully generated")
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName2,password))
        elif short_code == "dc":
            if display_accounts_details():
                print("")
                print("All your Credential accounts details: ")                
                print("")
                for account in display_accounts_details():
                    print(f" Account is:{account.account} \n User Name is:{userName2}\n Password is:{password}")
                    print("")
                print("")
            else:
                print("No credential account created")
        elif short_code == "sc":
            print("Enter the Credential Account Name (Eg twitter) to see more details")
            search_name = input()
            # if search_credential(search_name):
            
            if check_credentials(search_name): 
                global search_credential  
                search_credential = find_credential(search_name)
                print(f"For : {search_credential.account} account;")
                print(f"User Name is: {userName2} Password is:{search_credential.password}")
                print("")
            else:
                print("That Credential Account does not exist")
                print("")
        elif short_code == "del":
            print("Enter the account name of the Credential Account you wish to delete")
            search_name = input()
            if check_credentials(search_name):
                search_credential = find_credential(search_name)
                print("")
                search_credential.delete_credentials()
                print("")
                print(f"{search_credential.account} successfully deleted!!!")
                print("")
            else:
                print("Can't delete that Credential Account")

        elif short_code == 'gp':
            password = generate_Password()
            print(f" {password} Password generated successfully. Use it at your own pleasure")
        elif short_code == 'ex':
            print("Your passwords for credential account are now safe")
            break
        else:
            print("Wrong short code.")
    else:
        print("Enter correct input as guided to continue")
        

if __name__ == "__main__":
    main()    
