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

from random import random
from uuid import uuid4


def string_generator():
    return str(uuid4())

# Allow the user to input the name of their department that is used in the unique name.
department_name = input("Enter Department: Marketing, Accounting, FinOps: ")
for i in department_name:
    if department_name == "Marketing" or department_name == "marketing":
        print(f"We can always rely on {department_name} department to follow company naming convention")
        break
    elif department_name == "Accounting" or "accounting" == department_name:
        print(f"We can always rely on {department_name} department to follow company naming convention")
        break
    elif department_name == "FinOps" or "finOps" == department_name:
        print(f"We can always rely on {department_name} department to follow company naming convention")
        break

    else:
        print("Error: In order to use this generator, you enter the name correctly.\n"
              "Example: Marketing, Accounting, FinOps")
        exit()

# All the user to input how many EC2 instances they want names for and output the same amount of unique names.
number_of_ec2 = int(input("How many EC2 instances do you require?\n"))
if number_of_ec2 < 0:
    print("Please enter a positive number: ")
elif number_of_ec2 > 0:
    print(f"Creating {number_of_ec2} unique EC2 Instance Names")

# Generate random characters and numbers that will be included in the unique name.
for _ in range(1, number_of_ec2 + 1):
    unique_name = department_name
    EC2_unique_name = unique_name + "-" + string_generator()
    print("Your EC2 Instance's unique name is : ", EC2_unique_name)

