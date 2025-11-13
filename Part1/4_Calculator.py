# Please write a program which asks the user for two numbers and an operation.
#  If the operation is add, multiply or subtract,
#  the program should calculate and print out the result of the operation
#  with the given numbers.
#  If the user types in anything else,
#  the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2

# Write your code here:

nr1 = int(input("write the first nr:"))
nr2 = int(input("write the second nr:"))
op = input()
if (op=="add"):
    print(nr1 + nr2)
if (op=="multiply"):
    print(nr1 * nr2)
if ( op=="subtract"):
    print(nr1 - nr2)
    
