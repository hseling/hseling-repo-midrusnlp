import unittest

import hseling_api_midrusnlp


class HSELing_API_MidrusnlpTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_midrusnlp.app.test_client()

    def test_index(self):
        rv = self.app.get('/healthz')
        self.assertIn('Application MidRusNLP', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
