'''
Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique
so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the
users can then attach to the instances. The Python Script should:

1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
2. Allow the user to input the name of their department that is used in the unique name.
3. Generate random characters and numbers that will be included in the unique name.

ADVANCED
The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments.
List these departments as options and if a user puts another department, print a message that they should not use this
Name Generator. Be sure to account for incorrect upper or lowercase letters in the correct department.
Example: a user inputs accounting vs Accounting.

COMPLEX
Turn the above into a Function and execute the Function to verify it works.'''

from random import randint


# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
number_of_ec2s = input("How many EC2 instances do yuo require?\n")

# 2. Allow the user to input the name of their department that is used in the unique name.
department_name = input("What is your department name?\n")

# 3. Generate random characters and numbers that will be included in the unique name.

rand_ec2_namegen = randint(1, 1000)


'''
The randint() function is defined in the python random module can be used to create random strings within a range.
The function takes two numbers as its input argument. The first input argument is the #start of the range and the second
input argument is the #end of the range. 
After execution, the randint() function returns a random integer within the given range.
'''