# first part of the question
class Dog:
    quantity = 0 
    def __init__( self, name , age ):
        self.esm = name
        self.sen = age
        Dog.quantity += 1
        
bulldog = Dog('Sammy',3) 
hosky = Dog('Alex',5)
#hosky.quantity = 1  ---> this is the problem
print(Dog.quantity)
print(hosky.quantity)

# second part of question : کلاسی بنویسید که در یک متد ورودی از کاربر‌ بگیرد و در متدی دیگر ورودی گرفته‌شده
# و حفظ شده در کلاس را به صورت حروف بزرگ چاپ نماید

class TextProcess:
    def __init__(self):
        self.text = ""

    def user_input(self):
        self.text = input("Please enter some text: ")

    def vorodi_uppercase(self):
        print(self.text.upper())

temp = TextProcess()
temp.user_input()
temp.vorodi_uppercase()


