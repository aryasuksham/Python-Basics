# Basic practice programs for lists:

# Choosing an item from the list 
def buyFruits():
    fruits = ["Apple", "Banana", "Kiwi", "Cherry", "Orange", "Mango"]
    prices = [50, 40, 100, 120, 30, 60]

    for x in range(len(fruits)):
        print(fruits[x], prices[x])
            
    fruit = input("Enter the name of the fruit you want to buy: ")
    i = fruits.index(fruit)
    p = prices[i]

    bill = "You need to pay Rs.{} for {} at the counter."
    print(bill.format(p, fruit))

buyFruits()


# Inserting a new item and appending an item and a list 
def appendList():
    list1 = ["abc", "def", 34, 12, "xyz"]
    tuple1 = ("first", "second", 23)

    a = input("Enter an item to add in the list: ")

    list1.append(a)
    list1.insert(0, "kitt")
    list1.extend(tuple1)

    print(list1)

# appendList()


# Removing an item from the list and clearing it 
def removeList():
    list2 = ["cat", "dog", "rabbit", "spider", 90]
    print(list2)

    item = input("Enter the item to remove it from the list: ")

    if item.isdigit():
        finalItem = int(item)
        
    list2.remove(finalItem)
    index = int(input("Enter sn index to remove the item: "))
    list2.pop(index)

    finalQues = input("Do you want to empty the list(Yes/No): ")

    if finalQues == "Yes":
        list2.clear()
    
    print("Final list is: ",list2)

# removeList()


# Looping through List Comprehension and while loop
def listCom():
    list3 = ["BMW", "Ducati", "Yamaha"]
    list4 = ["Kawasaki", "Bajaj", "Hero"]

    [print(a) for a in list3 if 'a' in a]

    i = 0
    while i < len(list4):
        print(list4[i])
        i += 1
    
# listCom()


# Behaviour of different sorts and copying a list
def sortingList():
    list5 = ["apple", "Apple", "Bag", "yak"]

    # mylist = list5.copy()    #copy() and list() methods are used for copying a list
    mylist = list(list5)

    list5.sort()
    print("Simple Sort: ", list5)

    list5.sort(reverse = True)
    print("\nDescending Order: ", list5)

    list5.sort(key = str.lower)
    print("\nCase-Insensitive Sort: ", list5)

    list5.reverse()
    print("\nReverse Sort: ", list5)


# sortingList()



# Practice programs for tuples:

# Adding items in a tuple (as we know tuples are immutable)
def addToTuple():
    tuple1 = ("N160", "NS200", "N150")

    tempList = list(tuple1)
    tempList.append("H2")

    tuple1 = tuple(tempList)
    print("Modified Tuple: ", tuple1)

    tuple2 = ("H2R", "Panigale")

    tuple3 = tuple1 + tuple2
    print("We can add 2 tuples easily: ", tuple3)


# addToTuple()


# Removing an element from a tuple
def deleteFromTuple():
    t = ("a", "b", "c", "d")

    myList = list(t)
    myList.remove("d")

    t = tuple(myList)
    print("Modified tuple: ", t)

    res = input("Do you want to delete the tuple completely(Yes/No): ")

    if res == "Yes":
        del t
        # print(t)
    else:
        print("Thank you for your response.")


# deleteFromTuple()


# Unpacking a tuple (or list- both works same)
def unpackingTuple():
    myTuple = ("apple", "mango", "banana")
    res = input("Choose a case(1/2): ")

    if res == "1":
        (a, b, c) = myTuple
        print("Value of a: ", a)
        print("Value of b: ", b)
        print("Value of c: ", c)
    elif res == "2":
        (a, *b) = myTuple
        print("Value of a: ", a)
        print("Value of b: ", b)


# unpackingTuple()


# Programs for sets

# finding the intersection  of two lists
def intersectionOfLists():
    list1 = ["a", "b", "g"]
    list2 = ["g", "b", "k", 'l']
    
    set1 = set(list1)
    set2 = set(list2)

    set3 = set1.intersection(set2)
    set4 = set1.symmetric_difference(set2)

    list3 = list(set3)
    list4 = list(set4)
    print("Intersection of Lists: ", list3)
    print("Difference of Lists: ", list4)


# intersectionOfLists()


