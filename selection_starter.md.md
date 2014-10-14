#Starter - Selection Statements
These tasks are designed to refresh the reading and research you have undertaken at home prior to this lesson. If you have not completed the R&R assignment then please speak to your teacher before attempting these exercises.

##Relational and Boolean Operators
Relational and boolean operators are used to construct selection statements. Refresh your knowledge of these concepts by attempting the below tasks.

###Task 1
Match each relational operator to its description.

|Operator|Description|
|:------:|-----------|
|`==`|equal to|
|`<`|less than|
|`>`|greater than |
|`!=`|not equal to|
|`<=`|less than or equal to|
|`>=`|more than or equal to|

###Task 2
Look at each of the following expressions, without using a computer what would they evaluate to?

|Variable|Value|
|--------|:---:|
|`test_score`|54|
|`age`|18|

|Expression|Result|
|:--------:|:----:|
|`5 > 3`|True |
|`test_score < 12`|False |
|`4 != test_score`|True |
|`age == 17`|False |
|`test_score > 50 and age > 12`|True |
|`not test_score > 50`|False
 |

##Debugging Code
Debugging code is an important skill you must develop. The below will introduce you to **syntax**, **run-time** and **logical errors** that can occur in your code.

###Task 1
The code shown below contains some errors. Annotate the code to show where the errors occur.

```python
#test grading program
test_score = input("Please enter your test score: ")
if test_score > 40:#Should be ammended to if test_score >40 and <50.
    print("E grade")
elif test_score > 50:#test_score is still more than 40 so it will print the above statement instead of this one because it doesn't have boundaries and will just end. The correct syntax should be elif test_score >50 and <60.
    print("D grade")
elif test_score > 60:#Same problem as above. Should be test_score >60 and <70.
    print("C grade")
elif test_score > 70:#Should be test_score >70 and <80.
    print("B grade")
elif test_score > 80:
    print("A grade")
else:
    print("Fail")
```

###Task 2
Now, load the `selection_errors.py` Python file and attempt to run it - note down any error messages you encounter and attempt to explain them.

|Error Message|Explanation|
|------------|-----------|
|EOL error while scanning literal |The programmer forgot to end a string by missing a qouatation mark.  |
|Traceback error |The wrong data type was used. In this case the input was set to a string and not integer. |

###Task 3
Assuming that you have corrected the errors in `selection_errors.py`, run the program and enter a test score which will give an A grade. For example, 94. What happens? Use the space below for your explanation.

|Explanation|
|-----------|
|The output is still "E grade". This is because the first if statement prints "E grade" as long as the mark is over 40 meaning that because 94 is over 40 it will go with this statement and ignore the others. |

There are three types of error in `selection_errors.py`:

1. Syntax errors
2. Run-time errors
3. Logical errors

In the space below develop a definition of each type and state the type of each error in Tasks Two and Three.

###Task 4
Please read page 95 of the AS Computing textbook and then use the space below for your definitions.

|Error|Definition|
|-----|----------|
|Syntax error|This is when the program fails to compile due to incorrect syntax. |
|Run-time error|This is when a program crashes or gets stuck in a loop because the syntax used was correct but not used in the way the programmer wanted. |
|Logical error|This is when the programmers logic was incorrect but the program still appears to work, without giving the correct outputs. |

###Task 5
Indicate whether you think the errors in **Task 2 and 3** where syntax, run-time or logical errors.

|Error|Type|
|-----|----|
|Task 2 (error message 1)|Syntax Error |
|Task 2 (error message 2)|Syntax Error |
|Task 3 error|Logical Error |

##Summary
In this section you have debugged a selection statement and discovered that there are three types of errors: syntax, run-time and logical. You will encounter these errors repeatedly in your code so it is vital that you have an appreciation of the differences between them.

