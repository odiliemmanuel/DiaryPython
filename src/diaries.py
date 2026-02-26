import re

from diary import Diary


class Diaries():

    def __init__(self):
        self.__diaries = []
        self.__number_of_diaries = 0

    def get_number_of_diaries(self):
        return self.__number_of_diaries

    def add(self, username, password):
        self.validate_username(username)
        self.validate_password(password)
        diary = Diary(username, password)

        self.__diaries.append(diary)
        self.__number_of_diaries += 1

    def find_diary_with_username(self, username):
        for diary in self.__diaries:
            if diary.get_username() == username:
                return diary

        self.validate_find_username(username)
        return None


    def validate_find_username(self, username):
        for diary in self.__diaries:
            if diary.get_username != username:
                raise ValueError("Diary Not Found")



    def validate_password(self, password):
        for diary in self.__diaries:
            if not re.match("^[0-9]*$", password):
                raise ValueError("Invalid password")

    def validate_username(self, username):
        for diary in self.__diaries:
            if not re.match("^[A-Za-z]*$", username):
                raise ValueError("Invalid username")

    def delete(self, username, password):
        self.validate_username(username)
        self.validate_password(password)
        diary = self.find_diary_with_username(username)
        self.__diaries.remove(diary)

        self.__number_of_diaries -= 1