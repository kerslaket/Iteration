number = int(input("Please enter a number"))
facNum = 1
countNum = 1
for count in range(1, number):
    facNum = facNum * (countNum + 1)
    countNum += 1
print(facNum)
