from pswdmanage import User
from pswdmanage import Credentials
import unittest
# import our class from pswdmanage module

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('annet','annet254')

    def test_init(self):
        """
        The method checks if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'annet')
        self.assertEqual(self.new_user.password,'annet254')

    def test_save_user(self):
        """
        Test case to test if a new User instance has been appended to the User_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('Linkedin','annet_Renah','renah123')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Linkedin')
        self.assertEqual(self.new_credential.userName,'annet_Renah')
        self.assertEqual(self.new_credential.password,'renah123')
    def save_credential_test(self):
        """
        Test case to test presence credential object in the credentials_list items.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_delete_credential(self):
        """
        Test method to test a deleted credentials account is removed from the credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Codewar","nazarena","renah234")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)     
    def tearDown(self):
        '''
        Test method to test if deleted credential account has been cleared from credentials_list.
        '''
        Credentials.credentials_list = []       

if __name__ == "__main__":
    unittest.main()