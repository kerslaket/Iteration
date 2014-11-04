#Toby Kerslake
#28-10-2014
#Development Exercise 2

starNum = int(input("How many asterisks would you like to display per row"))
rowNum = int(input("How many rows of asterisks would you like to display"))

for count in range (0,rowNum):
    print("*" * starNum)
