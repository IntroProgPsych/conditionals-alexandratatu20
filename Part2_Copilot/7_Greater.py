# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5

# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8

# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

# Write your code here:

nr1 = int(input("write the first nr: "))
nr2 = int(input("write the second nr: "))
if (nr1 == nr2):
    print("The numbers are equal.")
elif (nr1>nr2):
    print(nr1)
else:
    print(nr2)
