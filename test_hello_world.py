import unittest
import hello_world as hw


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        s = 'Hello world'
        self.assertEqual(s, hw.hello_world(s))


