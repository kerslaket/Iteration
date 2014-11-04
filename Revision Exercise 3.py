#Toby Kerslake
#17-10-2014
#Revision Exercise 3

number = int(input("Please enter the amount of numbers you want averaged"))
average = 0

for count in range(number):
    number2 = int(input("Please enter a number"))
    average += number2

average2 = average / number2

print("Your average is {0}".format(average2))
