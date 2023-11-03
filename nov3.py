

# Crud operations on dictionaries
def crudDict():
    obj = {
        "Sam": {
            "company": "IT-Waves",
            "post": "FrontEnd Developer",
            "code": 101
        },
        "Sham": {
            "company": "IT-Waves",
            "post": "BackEnd Developer",
            "code": 102
        },
        "Raj": {
            "company": "IT-Waves",
            "post": "App Developer",
            "code": 103
        }
    }

    def case1():
        print("List of all employees':")
        [print(x) for x in obj.keys()]

    def case2():
        name = input("Enter the name of employee to see the record: ")
        print(obj[name])

    def case3():
        name = input("Name of the Employee: ")
        key = input("Enter the column to change: ")
        val = input("Enter the new value: ")

        obj[name][key] = val
        print("New record of the Employee:", obj[name])

    def case4():
        name = input("Name of the Employee: ")

        obj.pop(name)
        case1()

    caseObj = {
        1: case1,
        2: case2,
        3: case3,
        4: case4
    }
    res = int(input("What operation you want to perform:\nList of the employees: 1\nRecord of spefific employee: 2\nUpdate record of an employee: 3\nDelete record of an employee: 4\nPress the number: "))

    caseObj.get(res, lambda: print("Invalid Choice"))()
  

crudDict()


# Function implementation with arbitrary arguments (*args)
def arbFunction(*fruits):
    print("List of fruits available:")

    for x in fruits:
        print(x)


# arbFunction("apple", "kiwi", "papaya")  #we can pass list of items as an argument
    


# Function with Arbitrary Keyword Arguments (**kwargs)
def kwargFunction(**std):
    print("Name of the student is", std["name"])
    print("Age of the student is", std["age"])

# kwargFunction(name = "Swati", standard = 6, age = 11)


# Factorial of a number
def factFunction(num):
    # num = int(input("Enter a number to find factorial: "))
    
    res = 1
    if num > 0:
        res = num * factFunction(num-1)
    else:
       pass
    return res

# print(factFunction(4))


# Reverse of a string 
def reverseString(string):
    length = len(string)
    finalString = " "
    i = 1

    while i <= length:
        finalString += string[length-i]
        i += 1

    return finalString

# print(reverseString("student"))


# Lambda function- find simple interest
def myFun(p, t, r):
    return lambda : (p*t*r)/100

# x = myFun(5500, 2, 7)
# print(x())


