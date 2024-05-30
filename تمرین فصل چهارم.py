class Person:
    def __init__( self, name , age ):
        self.esm = name
        self.sen = age
    def display(self):
        print(self.esm , self.sen) 

class Student(Person):
    def __init__(self, name, age,major):
        super().__init__(name, age)
        self.reshte = major
    
    def displayStudent(self):
        print (self.esm , self.sen ,self.reshte)

obj1 = Person('hassan', 22)
obj2 = Student('abbas', 42 , 'computer engineering')

Person.display(obj1)
Student.displayStudent(obj2)