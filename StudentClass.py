from datetime import date, datetime


class Student:
    def __init__(self, Id, Name, DoB, Class):
        self.__studentID = Id
        self.__name = Name
        self.__dob = DoB
        self.__classification = Class
        self.__age = 0
        self.__register = ''

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_studentid(self):
        return self.__age

    def get_birthday(self):
        return self.__dob

    def get_register(self):
        return self.__register

    def get_age(self):
        return self.__age

    def register(self):
        if self.__classification == 'Sr':
            self.__register = "Registration is 11/1-11/3"
        elif self.__classification == 'Jr':
            self.__register = "Registration is 11/4-11/6"
        elif self.__classification == 'S':
            self.__register = "Registration is 11/7-11-9"
        elif self.__classification == 'F':
            self.__register = "Registration is 11/10-11/12"
        else:
            self.__register = "Classification is not recognized"

    def age(self):
        today = date.today()
        bday = self.__dob.split("/")
        bdayyear = int(bday[2])
        age = today.year - bdayyear
        self.__age = age
