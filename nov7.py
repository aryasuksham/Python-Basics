
# Exception Handling
def excepFun():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = [2, 3, 5]
        print(c[a])
        return a - b
   
    except ValueError:
        print("Error: You can only enter integer values.")
    except IndexError:
        print("Index Error has occurred.")

# print(excepFun())


# Exception Handling:- Example2
def exceptionFun():
    try:
        a = int(input("Enter first number: "))
        k = [11, 33]
        print(k[a])
        print(a*a)

    except Exception as e:
        print("Error:", e)

    else:
        print("Everthing went well:)")

# exceptionFun()


# Raising custom error
def customError():
    a = input("Do you want to continue with this technology(Y/N): ")

    if a != "Y" and a != "N" and a != "y" and a != "n":
        raise ValueError("You can only response with Y/N")
    
    print("Thank you for your response")

# customError()


# 'finally' in exception handling
def finFunction():
    try:
        x = int(input("Enter total marks: "))
        y = int(input("Enter marks obtained: "))
        z = (y/x)*100
        print("Percentage is", z)

    except:
        print("Error: Something went wrong:(")

    finally:
        print("Thank you for using our site")

# finFunction()


# File Handling 
import os

def fileReadFun():

    f = open("demofile.txt", "r")  #"r"- return an error if file does not exist
    print(f.read())
    f.close()

    # print(os.getcwd())
    # print('demofile.txt: ', os.path.basename(__file__))


# fileReadFun()


def fileWriteFun():

    f1 = open("demofile.txt", "x")  #"x"- return an error if the file exist
    f2 = open("demofile.txt", "a")  #"a"- creates the file if does not exist and append the text
    f3 = open("demofile.txt", "w")  #"w"- cretes file if doesn't exist and overwrite the existing content

    f2.write("Hello and welcome to this file.\n")


# fileWriteFun()


def fileDeleteFun():

    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")     
    else:
        print("File does not exists")


fileDeleteFun()


