import random

class Insect:
    def __init__(self, w, l):
        self.wings = w
        self.legs = l
        self.length = 0


    def fly(self):
        self.length = random.randint(1,10)


    def get_length(self):
            return self.length