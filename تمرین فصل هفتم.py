from abc import ABC,abstractmethod
import random
import string

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class OnlyLetter(PasswordGenerator):
    def __init__(self):
        super().__init__() 
    def generate(self):
        n = 20
        res = ''.join(random.choices(string.ascii_letters, k=n))
        return res
        
    
class OnlyDigits(PasswordGenerator):
    def __init__(self):
        super().__init__()
    def generate(self):
        n = 20
        res = ''.join(random.choices(string.digits, k=n))
        return res

class LetterDigits(PasswordGenerator):
    def __init__(self):
        super().__init__()
    def generate(self):
        n = 20
        res = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
        return res
    
only_letter_generator = OnlyLetter()
only_digits_generator = OnlyDigits()
letter_digits_generator = LetterDigits()

print("Only Letters: ", only_letter_generator.generate())
print("Only Digits: ", only_digits_generator.generate())
print("Letters and Digits: ", letter_digits_generator.generate())