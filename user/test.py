class User(unittest.TestCase):
    """unit tests: user function."""

    def test_user():
        """Test user function.""" 
        self.assertEqual(user.user(), 'user')
        
        
if __name__ == "__main__":
    unittest.main(
        # testRunner=xmlrunner.XMLTestRunner(output=os.environ.get('CIRCLE_TEST_REPORTS','test-reports')),
        testRunner=xmlrunner.XMLTestRunner(output='user'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)          
