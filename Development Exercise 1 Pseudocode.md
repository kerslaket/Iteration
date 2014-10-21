##Development Exercise 1

###Pseudocode

GET number
facNum = 1
countNum = 1
FOR i <--- 1 - number
facNum = facNum * (countNum + 1)
countNum += 1
OUT facNum

###Test Tables

|Input|Expected Output|Actual Output|Match?|
|----|----|----|----|
|5|120|120|Yes|
|4|24|24|Yes|
|-4|Error|-1|No|
|as|Error|Error|Yes|

> Written with [StackEdit](https://stackedit.io/).