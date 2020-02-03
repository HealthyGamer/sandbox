from unittest.mock import patch
from unittest import TestCase

from sandbox.quizz import run


class TestQuizz(TestCase):
    @patch('builtins.input', return_value='a')
    def test_correct_answer(self, input):
        self.assertTrue(run())

    @patch('builtins.input', return_value='b')
    def test_wrong_answer(self, input):
        self.assertFalse(run())


if __name__ == '__main__':

    TestQuizz().run()
