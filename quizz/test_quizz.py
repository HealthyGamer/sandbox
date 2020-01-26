from unittest.mock import patch
from unittest import TestCase

from main import quizz


class TestQuizz(TestCase):
    @patch('builtins.input', return_value='a')
    def test_correct_answer(self, input):
        self.assertTrue(quizz())

    @patch('builtins.input', return_value='b')
    def test_wrong_answer(self, input):
        self.assertFalse(quizz())
