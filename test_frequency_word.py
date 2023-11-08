import unittest
from frequency_word import frequency_word


class TestFrequencyWord(unittest.TestCase):
    def test_frequency_word(self):
        result = frequency_word(3, "apple banana banana cherry apple cherry")
        expected = [(2, 'banana'), (2, 'cherry'), (2, 'apple')]
        self.assertCountEqual(result, expected)

        result = frequency_word(5, "")
        expected = []
        self.assertCountEqual(result, expected)

        result = frequency_word(4, "       ")
        expected = []
        self.assertCountEqual(result, expected)

        result = frequency_word(0, "apple banana banana cherry apple cherry")
        expected = []
        self.assertCountEqual(result, expected)

        result = frequency_word(2, "apple banana banana cherry apple cherry")
        expected = [(2, 'banana'), (2, 'cherry')]
        self.assertCountEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
    