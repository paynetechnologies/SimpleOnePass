import unittest
from src.globals import constants, entry

class postfixTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()\

    def test_can_start(self):
        self.assertTrue("test starting...")

if __name__ == '__main__':
    unittest.main(warnings='ignore')        