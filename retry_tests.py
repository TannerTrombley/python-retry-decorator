import unittest
from retry import retry_operation

class RetryBasicTests(unittest.TestCase):

    def test_basic(self):
        @retry_operation(Exception)
        def operation():
            print("Operation running")
            raise Exception()

        with self.assertRaises(Exception):
            operation()

    def test_linear(self):
        @retry_operation(Exception, backoff_factor=1)
        def operation():
            print("operation")
            raise Exception()
        with self.assertRaises(Exception):
            operation()


if __name__ == "__main__":
    unittest.main()