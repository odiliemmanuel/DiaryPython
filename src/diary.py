import re

from src.entry import Entry


class Diary:
    def __init__(self, password):
        self.__number_of_entries = 0
        self.__entries : list[Entry] = []
        self.__password = password
        self.__is_locked = False
        self.__id = 1

    def lock_diary(self):

        self.__is_locked = False

    def is_locked(self):
        return self.__is_locked

    def unlock_diary(self, password):
        self.validate_password(password)
        self.validate_correct_pin(password)
        if self.__password == password:
            self.__is_locked = True


    def validate_password(self, password):
        if not re.fullmatch("\\d{4}", password):
            raise ValueError("Invalid password")



    def validate_correct_pin(self, password):
        if self.__password != password:
            raise ValueError("Invalid password")



    def create_entry(self, title, body):
        if self.__is_locked:
            entry = Entry(self.__id, title, body)

            self.__entries.append(entry)
        self.__number_of_entries += 1
        self.__id += 1

    def get_number_of_entries(self):
        return self.__number_of_entries

    def delete_entry(self, id):
        for entry in self.__entries:
            if entry.get_id() == id:
                self.__entries.remove(entry)
                self.__number_of_entries -= 1
            else:
                raise ValueError("Id not Found")




