#Toby Kerslake
#30-10-2014
#Stretch And Challenge Exercise 4

number = int(input("Please enter a number:"))
counter = 0
numList = []


for count in range(number):
    counter += 1
    counter2 = counter * counter
    numList.insert(counter,counter2)
    length = len(numList)

while length > 0:
    print(numList[0:5])
    numList.pop(0)
    numList.pop(0)
    numList.pop(0)
    numList.pop(0)
    numList.pop(0) 
