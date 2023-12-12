import unittest
from src.ans import transform_quote

class TestTransformativeQuote(unittest.TestCase):
    def test_quote_transformation(self):
        quote = "To be or not to be"
        expected = "TO_BE_OR_NOT_TO_BE18"
        self.assertEqual(transform_quote(quote), expected)

# Additional tests might include quotes with punctuation, very long quotes, or quotes with no spaces.


if __name__ == '__main__':
    unittest.main()
