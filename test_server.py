import server
import unittest


class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes."""

    def test_index(self):
        """Make sure index page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()
        server.app.config['TESTING'] = True

            # Use the test client to make requests
        result = client.get('/')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Welcome</h1>', result.data)

    def test_form(self):
        """Test that / route processes form data correctly."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.post('/', data={'person': 'Henna'})
        self.assertIn(b'Henna', result.data)  

class MyTest(unittest.TestCase):
    def test_index(self):
        client = server.app.test_client()
        server.app.config['TESTING'] = True

        result = client.get('/')
        self.assertEqual(result.status_code, 200)  

    def test_index_post(self):
        client = server.app.test_client()
        server.app.config['TESTING'] = True

        result = client.post('/', data={'person': 'Henna'})
        self.assertEqual(result.status_code, 200)     


if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output=os.environ.get('CIRCLE_TEST_REPORTS','test-reports')),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)        