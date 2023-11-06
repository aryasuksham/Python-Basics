
from functools import reduce


# map, filter and reduce with lambda function
def myFun():

    x = [2, 5, 7, 8]

    ans = list(map(lambda a: a*a, x))
    print("Squares of the list:", ans)

    ans1 = list(filter(lambda b: b>5, x))
    print("Greater than b:", ans1)

    ans2 = reduce(lambda c, d: c+d, x)
    print("Sum of the list:", ans2)

# myFun()


# Class:- simple example with constructor
class mobileDetails:
    def __init__(self, model, ram, screen):
        print("Welcome Everyone")
        self.model = model
        self.ram = ram
        self.screen = screen

    def info(self):
        print(f"{self.model} has {self.ram} GB RAM.")

# a = mobileDetails("j2", 6, 8)
# a.info()



# Decorator function
def greet(fn):
    def wrapper(*args, **kwargs):
        print("Good Morning")
        fn(*args, **kwargs)
        print("Thanks for coming :)")
    return wrapper


@greet
def add(a,b):
    print("Sum is:",a+b)
    return a+b
# greet(add)(2,3)

@greet
def printingHello():
    print("Hello")
    
# add(1,3)
    


# Inheritance:- Example
class Student:
    def __init__(self, name, standard, rollNo):
        self.name = name
        self.standard = standard
        self.rollNo = rollNo
    def intro(self):
        return f"{self.name} studies in class {self.standard}"

a = Student("Kapila", 7, 21)
# print(a.intro())

class MStudent(Student):
    def __init__(self, name, mark1, mark2, standard, rollNo):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        # Student.__init__(self, name, standard, rollNo)  #all properties and methods can be inherited using this method also
        super().__init__(name, standard, rollNo)

    def sum(self):
        return self.mark1 + self.mark2


b = MStudent("Kashi", 83, 88, 5, 21)
# print(b.intro())
# print(b.sum())



# Inheriting multiple classes
class Person:
    def __init__(self, fname, lname, age, height):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height

    def fullName(self):
        return f"{self.fname} {self.lname}"

    def getAge(self):
        return f"Age is {self.age}"

    
class Teacher:
    def __init__(self, school, subject):
        self.school = school
        self.subject = subject

    def getSub(self):
        return f"{self.subject} subject teacher"


class StudentClass(Person, Teacher):
    def __init__(self,marks,sId, fname, lname, age, height, school, subject):
        self.marks = marks
        self.sId = sId
        Person.__init__(self, fname, lname, age, height)
        Teacher.__init__(self, school, subject)

    def getId(self):
            print(f"Id of student named {self.fname} is {self.sId}")


# abc = StudentClass(23, 10001, "Lewis", "Tan", 13, 159, "GHS", "CS")
# abc.getId()


# Modules
import datetime
def dateFun():
    d = datetime.datetime.now()
    print("DateTime is:",d)

    exec = d.strftime('%B')
    print(exec)

    exec1 = d.strftime('%A')
    print(exec1)

# dateFun()



# JSON Conversion
import json

def JSONConversion():
    tempDict = {
        "name": "arya",
        "club": "dev07",
        "code": 35
    }

    finalJson = json.dumps(tempDict)   #Python to JSON conversion
    print(finalJson)

    pyDict = json.loads(finalJson)   #JSON to Python conversion
    print(pyDict)

JSONConversion()