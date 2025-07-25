# a=31
# print(a)
# from xml.sax.handler import property_interning_dict

# Calculator using python

# a=input(""Enter first number: ")
# b=input("Enter second number: ")
# c=input("Enter operator: ")

# if c=='+':
#     print(float(a)+float(b))
# elif c=='-':
#     print(float(a)-float(b))
# elif c=='*':
#     print(float(a)*float(b))
# elif c=='/':
#     print(float(a)/float(b))
# elif c=='//':
#     print(float(a)//float(b))
# elif c=='%':
#     print(float(a)%float(b))
# elif c=='**':
#     print(float(a)**float(b))
# else:
#     print("Invalid operator")


# Typecasting in python

# a = "3"
# b = "25"
# print(float(a)+float(b))
# print(a+b)  # This will concatenate the strings



#  User input in python


# a = input("Enter your name: ")
# print("Hello, " + a + "!")  # This will concatenate the strings

# x = int(input(""Enter first number: "))
# y = int(input("Enter second number: "))
# print(x + y)

# Strings in python

# name = input("Enter your name: ")
# # print("My name is " + name + ".")
# print(name[1])
# print(name[0])
# print(name[2])
# print(name[3])



# for character in name:
#     print(character)




# String slicing in python

# name = "Priyanshu"
# print(names[9:14])  # Priyanshu
# print(len(names))  # Length of the string

# print(name[-8:-4])




# String methods in python

# Strings are immutable in python, meaning they cannot be changed after creation.

# x = "priyanshu::::::" 
# print(len(x))  # Length of the string
# print(x.upper())
# print(x.lower())
# print(x.rstrip(":"))  # Removes trailing whitespace
# print(x.capitalize())  # Capitalizes the first letter

# print(x.replace("priyanshu", "Priyanshu"))  # Replaces a substring with another

# st1 = "Welcome to India !!!"
# print(st1.endswith("!!!"))  # Checks if the string ends with "!!!"
# print(st1.endswith("to",4,10))  





# if else statements in python

# you can vote or not

# age = int(input("Enter your age:"))
# print("Your age is:", age)
#
# if age>18:
#     print("You can vote.")
# else:
#     print("You can't vote.")
  

  
# Conditional Operators
# >, <, >=, <=, ==, !=


# Checking criteria by if else

# Mobile_Price = float(input("Enter the price: "))
#
# Budget = 45000.50
#
# if Mobile_Price<=Budget:
#     print("Aukat me hai!!!")
# else:
#     print("Aukat banao jaa ke pehle!!!!!!!!!!!!1")



# if elif else

# x = float(input("Enter the number: "))
#
# if x<0:
#     print("the number is negative")
# elif x==0:
#     print("the number is equal to zero")
# elif x==69:
#     print("the number is sexyyyy!")
# else:
#     print("the number is positive")
#
# print("Ooooo yeah..........")





# from turtle import *
# import colorsys
#
# speed (0)
# bgcolor("black")
# h= 0
# for i in range(16):
#     for j in range(18):
#         c = colorsys.hsv_to_rgb(h, 1, 1)
#         color(c)
#         h += 0.005
#         rt(90)
#         circle(150 - j * 6, 90)
#         lt(90)
#         circle(150 - j * 6, 90)
#         rt(180)
#     circle(40, 24)
# done()




# nested if else:

# x = float(input("enter the no.: "))
#
# if x < 0:
#     print("the no. is -ve")
# elif x > 0:
#     if x <=20:
#         print("the no. is b/w 1-20")
#     elif x > 20 and x <= 50:
#         print("the no. is b/w 21-50")
#     else:
#         print('the no. is greater the 50')
# else:
#     print("the no. is special.")



#  Exercise-2

# import time
# from datetime import datetime
#
# current_time = datetime.now().hour
#
# if 5 <= current_time <12:
#     print("Good Morning!")
# elif 13 <= current_time <17:
#     print("Good Afternoon!")
# elif 17 <= current_time <21:
#     print("Good Evening!")
# else:
#     print("Good Night!")


# For loop


# cars = ["BMW", "Porsche", "Buggati", "Fararei"]
# for car in cars:
#     print(car)
#     for i in car:
#         print(i)


# for i in range(1, 20001):
#     print(i)

# for x in range(5, 15, 2):
#     print(x)


# while loop


# x = 60
# while x<70:
#     print(x)
#     x+=1

# x = 1
#
# while x<51:
#     print(x)
#     x+=1


# x = int(input("Enter the no.: "))
# while(x<=20):
#     x = int(input("Enter the no.: "))
#     print(x)
# print(("Loop over!"))

# x = 15
# while x > 0:
#     print(x)
#     x-=3



# table using for loop
# x = int(input(""Enter the no. to print the table of: "))
# for i in range(1, 21):
#     print(x, "x", i, "=", x*i)



# loops questions

# 1. Table:

# for i in range(10):
#     print("5 X", i+1, "=",  5 * (i+1) )

# code greet to the person with letter S

# l = ["Priyanshu", "Pranjal", "Smrutirupa", "Nyayabrata", "Abhipsa", "Rudra"]
#
# for name in l:
#     if name.startswith("P"):
#         print("Hello", name+'!')


# table using while loop
# x = int(input("Enter the no.: "))
# i=1
# while i<=10:
#     print(x, "x", i, "=", x*i)
#     i+=1


# no. is prime or not











# Functions in python:

# def calculateGmean(x, y):
#     mean = (x*y)/(x+y)
#     print(mean)
#
#
# a = 10
# b = 9
#
# calculateGmean(a, b)


# isGreater function

# def isGreater(a, b, c):
#     if (b<a>c):
#         print("the 1st no. is greater")
#     elif (a<b>c):
#         print("the 2nd no. is greater")
#     else:
#         print("the 3rd no. is greater")
#
#
# a = int(input("enter the no.: "))
# b = int(input("enter the no.: "))
# c = int(input("enter the no.: "))
#
# isGreater(a, b, c)


# ch-2 practice

# Q1.

# a = int(input(""Enter the 1st no.: "))
#
# b = int(input("Enter the 2nd no.: "))
#
# print(a+b)


# Q2.

# x = int(input("Enter the no.: "))
#
# y = int(input("Enter the no.: "))
#
# z = x%y
#
# print(z)


# Q3.

# x = input()
#
# print(type(x))


# Q4.

# x = int(input("Entr the 1st no.: "))
#
# y = int(input("Entr the 2nd no.: "))
#
# z = (x+y)/2
#
# print(int(z))


# Q5.

# a = int(input("Enttr the no.: "))
#
# print(a**2)

# ch-3 practice

# Q1.

# hi = input("entr the name: ")
#
# print("Good Afternoon!"+' '+hi)


# Q2.


# Name = input("Enter the name: ")
# Date = (input())
#
# letter = f"""
#          Dear {Name},
#          You are selected!
#          {Date}.
#          """
# print(letter)


# my_string = input("Enter a string: ")
#
# # Check if double spaces exist
# if "  " in my_string:
#     print("Double spaces found in the string!")
# else:
#     print("No double spaces found in the string.")

# Ch-4 practice

# Q1.

# fruits = []
#
# for i in range(1, 8):
#     fruit = input(f"Enter fruits{i}: ")
#     fruits.append(fruit)
# print(fruits)

# Q2.

# marks = []
#
# for i in range(1,6):
#     mark = int(input(f"enter the marks{i}: "))
#     marks.append(mark)
#
# marks.sort()
#
# print(marks)


# Q3.

# Functions arguments...

# def avg(a=4 ,b=5):
#     print("The average is: ", (a+b)/2)
#
#
# avg(5,5)


# Lists in python

# names = ["Priyanshu", "Ansh", "Smruti", "Kunnu","Abhipsa"]

# print(type(names))
# print(names[0])


# If there is a negative index then 1st convert it to +ve

# lst1 = [i for i in range(15) if i%3==0]
# print(lst1)


# list methods

# a = [11, 15, 19, 23, 16]
#
# a.append(2)
# a.sort()
#
# print(a)

# Tuple in python

# t = (15, 22, 36, 66, 58)

# print(type(t), t)


# fstring in pythorn

# greetme = "Hey {1}, How are you?"
#
# name = input("Enter the name: ")
#
# print(f"Hey {name}, How are you?")


# Recursion

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(6))

# Set in python

# pri = set()
#
# print(type(pri))

# set methods

# set1 = {15,25,35,45,85}
#
# set2 = {36,45,12,65}
#
# print(set1.union(set2))

# set1.update(set2)

# print(set1)

# set1.intersection_update(set2)
#
# print(set1)

# print(set1.isdisjoint(set2))


# Dictionaries in python

# Dictionaries are key-value pairs that are separated by commas and enclosed within curly braces{}.

# Example

dict = {
    "Name": "Priyanshu",
    "Age": 22,
    "Profession": "Student"
}

# print(dict["Age"])




























