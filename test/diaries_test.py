import unittest

from diaries import Diaries


class DiaryTest(unittest.TestCase):

    def setUp(self):
        self.my_diaries = Diaries()


    def test_that_diary_is_empty(self):
        self.assertEqual(0,self.my_diaries.get_number_of_diaries())


    def test_that_i_can_add_to_my_diaries_and_list_of_diaries_increases(self):
        self.assertEqual(0, self.my_diaries.get_number_of_diaries())
        self.my_diaries.add("David", "7765")
        self.assertEqual(1, self.my_diaries.get_number_of_diaries())


    def test_that_i_can_find_diary_with_username(self):
        self.assertEqual(0, self.my_diaries.get_number_of_diaries())

        self.my_diaries.add("David", "7765")
        self.my_diaries.add("John", "3342")
        self.my_diaries.add("Iris", "7798")

        self.assertEqual(3, self.my_diaries.get_number_of_diaries())

        self.assertEqual("John", self.my_diaries.find_diary_with_username("John").get_username())


    def test_that_while_finding_diary_if_diary_does_not_exist_error_is_thrown(self):
        self.assertEqual(0, self.my_diaries.get_number_of_diaries())

        self.my_diaries.add("David", "7765")
        self.my_diaries.add("John", "3342")
        self.my_diaries.add("Iris", "7798")

        self.assertEqual(3, self.my_diaries.get_number_of_diaries())

        with self.assertRaises(ValueError):
            self.my_diaries.find_diary_with_username("Daniel")


    def test_that_i_can_delete_a_diary_and_number_of_diaries_decreases(self):
        self.assertEqual(0, self.my_diaries.get_number_of_diaries())

        self.my_diaries.add("David", "7765")
        self.my_diaries.add("John", "3342")
        self.my_diaries.add("Iris", "7798")

        self.assertEqual(3, self.my_diaries.get_number_of_diaries())

        self.my_diaries.delete("David", "7765")
        self.assertEqual(2, self.my_diaries.get_number_of_diaries())


    def test_that_I_cannot_delete_an_entry_that_doesnt_exist(self):
        self.assertEqual(0, self.my_diaries.get_number_of_diaries())

        self.my_diaries.add("David", "7765")
        self.my_diaries.add("John", "3342")
        self.my_diaries.add("Iris", "7798")

        self.assertEqual(3, self.my_diaries.get_number_of_diaries())

        self.assertRaises(ValueError, self.my_diaries.delete, "Jooj", "9865")



