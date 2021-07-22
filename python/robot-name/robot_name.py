import string
import random


class Robot:
    
    def __init__(self):
        self.name = self.generator()

    def generator(self):
        return "".join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))

    def reset(self):
        while True:
            newname = self.generator()
            if newname != self.name:
                break
        self.name = newname
