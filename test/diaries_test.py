import unittest

from diaries import Diaries


class DiaryTest(unittest.TestCase):

    def setUp(self):
        self.my_diaries = Diaries()


    def test_that_diary_is_empty(self):
        self.assertEqual(0,self.my_diaries.get_number_of_diaries())