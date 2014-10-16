# program to prompt for 8 numbers and report the total to the user

total = 0
num = 0

for count in range(8):
    num = int(input("Please enter a number"))
    total += num


print('The total is {0}'.format(total))


