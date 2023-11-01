"""Starting Basics of Python
   All New Programs/Functions will be added here Ragularly"""

import random


# Generating password/OTP
def generatingPasswordOrOTP():
  userName = input("Please enter your name: ")
  # print("Hello " + userName +". Welcome to the Sky High")
  greet = "Hello {}. Welcome to the Sky High"
  print(greet.format(userName))

  def checkName():
     if len(userName)>1:
        return userName[0:3]
    
     else:
        print("Incorrect Name! Please try again")
        return False

  name = checkName()

  def generateOTP():
      randomNumber = str(random.randrange(11111, 99999))
      otp = checkName() + randomNumber
      return otp

  if name:
      print("OTP is: " +generateOTP())


# generatingPasswordOrOTP()

#Converting Snake case into Pascal case
def snakeToPascal():
    string = input("Please enter a string in snake case (eg. ab_cd): ")
    string1 = string.replace("_"," ")
    result = string1.title().replace(" ","")
    print("String in Pascal case: " +result)

# snakeToPascal()    


# Checking if substring is present in the string
def substringCheck():
    name = input("Please enter your name: ")
    registerationNumber = input("Now enter your registeration number: ")

    tempStr = name[:3]
    # checkingReg = registerationNumber.find(tempStr)

    if tempStr in registerationNumber:
        phone = int(input("Enter your mobile number: "))
        # if type(phone) == int:
        #     print("Thank you for submitting details.")
        # else:
        #     print("Format of phone number is wrong")
    else: 
        print("Something went wrong. Please try again")

# substringCheck()        


# To interchange or swap 2 elements in a list
def swappingTwoElements():
    list1 = ["abc", "def", "ghi", "jkl"]

    element1 = "abc"
    element2 = "ghi"
    pos1 = list1.index(element1)
    pos2 = list1.index(element2)

    list1[pos1] = element2
    list1[pos2] = element1
    print(list1)


swappingTwoElements()