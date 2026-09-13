#Task 3 - Simple Class and Inheritance

#Lager Person class, bruker samme oppsett som i PRO1002 3.3 Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, My name is {self.name} and I am {self.age} years old.")

#Lager student class objektet som arver attributter fra person class (eksempel under PRO1002 3.3 Inheritance)
 
class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id

student = Student("Kristine", 38, "3001814")

student.greet()
print(f"Student ID: {student.student_id}")

#printer både greet og student ID. Mulig jeg kunne løst det litt annerledes, og lagt inn alt i samme greet?