
import unittest
import xmlrunner
import helpers



# class User(unittest.TestCase):
#     """unit tests: user function."""

#     def test_user():
#         """Test user function.""" 
#         self.assertEqual(user.user(), 'user')
        
class TestHelpers(unittest.TestCase):
    """unit tests: helper functions."""

    def test_is_person(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('Henna'), True)
#         self.assertEqual(helpers.is_person('. '), True)
    def a(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('User'), True)
    def b(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('Henna'), True)
#         self.assertEqual(helpers.is_person('. '), True)
    def z(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('Henna'), True)            
        
        
if __name__ == "__main__":
    unittest.main(
        # testRunner=xmlrunner.XMLTestRunner(output=os.environ.get('CIRCLE_TEST_REPORTS','test-reports')),
        testRunner=xmlrunner.XMLTestRunner(output='user'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)          
