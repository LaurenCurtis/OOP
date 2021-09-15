class Student:
    def __init__(self, Id, Name, DoB, Class):
        self.__studentID = Id
        self.__name = Name
        self.__dob = DoB
        self.__classification = Class

    def register (self):
        if self.__classification == 'Sr':
            print("Registration is 11/1-11/3")
        elif self.__classification == 'Jr':
            print("Registration is 11/4-11/6")
        elif self.__classification == 'S':
            print("Registration is 11/7-11-9")
        elif self.__classification == 'F':
            print("Registration is 11/10-11/12")
        else:
            ("Classification is not recognized")