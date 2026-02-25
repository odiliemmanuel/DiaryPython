import unittest

from src.diary import Diary



class DiaryTest(unittest.TestCase):

    def setUp(self):
        self.my_diary = Diary("7789")

    def test_that_diary_is_locked(self):
        self.my_diary.lock_diary()
        self.assertFalse(self.my_diary.is_locked())


    def test_that_diary_can_be_unlocked(self):
        self.assertFalse(self.my_diary.is_locked())

        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())


    def test_that_while_unlocking_diary_if_password_is_incorrect_error_is_thrown(self):
        self.assertFalse(self.my_diary.is_locked())

        with self.assertRaises(ValueError):
            self.my_diary.unlock_diary("7725")



    def test_that_entry_can_be_created_and_list_of_entries_increases(self):
        self.assertFalse(self.my_diary.is_locked())

        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("The Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")

        self.assertEqual(2, self.my_diary.get_number_of_entries())


    def test_that_delete_an_entry_and_size_of_entry_decreases(self):
        self.assertFalse(self.my_diary.is_locked())

        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")
        self.my_diary.create_entry("Love", "She said that she loves me and asked for dating")
        self.my_diary.create_entry("Book", "The book i read today is quite an interesting one")

        self.assertEqual(4, self.my_diary.get_number_of_entries())

        self.my_diary.delete_entry(2)
        self.assertEqual(3, self.my_diary.get_number_of_entries())


    def test_that_if_i_try_to_delete_an_entry_that_doesnt_exist_error_is_thrown(self):
        self.assertFalse(self.my_diary.is_locked())

        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")
        self.my_diary.create_entry("Love", "She said that she loves me and asked for dating")
        self.my_diary.create_entry("Book", "The book i read today is quite an interesting one")

        self.assertEqual(4, self.my_diary.get_number_of_entries())

        with self.assertRaises(ValueError):
            self.my_diary.delete_entry(5)
        self.assertEqual(4, self.my_diary.get_number_of_entries())


    def test_that_i_can_find_entry_using_its_id(self):
        self.assertFalse(self.my_diary.is_locked())

        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")
        self.my_diary.create_entry("Love", "She said that she loves me and asked for dating")
        self.my_diary.create_entry("Book", "The book i read today is quite an interesting one")

        self.assertEqual(4, self.my_diary.get_number_of_entries())

        self.assertEqual("Love", self.my_diary.find_entry(3).get_title())


    def test_that_while_finding_entry_if_entry_does_not_exist_error_is_thrown(self):
        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")
        self.my_diary.create_entry("Love", "She said that she loves me and asked for dating")
        self.my_diary.create_entry("Book", "The book i read today is quite an interesting one")

        self.assertEqual(4, self.my_diary.get_number_of_entries())

        with self.assertRaises(ValueError):
            self.my_diary.find_entry(6)

        self.assertEqual("Love", self.my_diary.find_entry(3).get_title())


    def test_that_i_can_update_entry(self):
        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")
        self.my_diary.create_entry("Love", "She said that she loves me and asked for dating")
        self.my_diary.create_entry("Book", "The book i read today is quite an interesting one")

        self.assertEqual(4, self.my_diary.get_number_of_entries())

        self.my_diary.update_entry(3, "Flash", "Fastest man alive")
        self.assertEqual("Flash", self.my_diary.find_entry(3).get_title())



    def test_that_while_updating_diary_and_it_doesnt_exist_error_is_thrown(self):
        self.my_diary.unlock_diary("7789")
        self.assertTrue(self.my_diary.is_locked())

        self.my_diary.create_entry("Break_up", "She said that she doesnt like me again")
        self.my_diary.create_entry("Money", "I got money yesterday")
        self.my_diary.create_entry("Love", "She said that she loves me and asked for dating")
        self.my_diary.create_entry("Book", "The book i read today is quite an interesting one")

        self.assertEqual(4, self.my_diary.get_number_of_entries())

        with self.assertRaises(ValueError):
            self.my_diary.update_entry(8, "Flash", "Fastest man alive")



