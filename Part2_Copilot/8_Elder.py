# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Write your code here:

name1 = input("1st name: ")
age1 = int(input("1st age: "))
name2 = input("2nd name: ")
age2 = int(input("2nd age: "))
if (age1 == age2):
    print(name1 , "and" , name2, "are the same age.")
elif (age1>age2):
    print("The elder is" , name1)
else:
    print("The elder is" , name2)

