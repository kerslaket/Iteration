#Toby Kerslake
#30-10-2014
#Development Exercise 4

##Write a program that finds the largest of a series of numbers.
##Ask the user to enter a series of numbers, entering the rogue value -1
##when they have finished. Then report the largest value to the user

number = 0
number2 = 0
while number2 != -1:
    number2 = int(input("Please enter a number"))
    if number2 > number:
        number = number2
print("The largest number is {0}".format(number))
