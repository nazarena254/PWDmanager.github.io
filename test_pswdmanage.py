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

if __name__ == "__main__":
    unittest.main()