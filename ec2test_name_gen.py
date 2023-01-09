
'''
Finished EC2 name gen, now I want to create a while loop that alleviates the need to re-run the app every time its
needed. I also want to move all the logic to a sep module that will be call upon
'''

from uuid import uuid4


def string_generator():
    return str(uuid4())


def validate_dept_name(department):
    for i in department:
        if department == "Marketing" or department == "marketing":
            print(f"We can always rely on {department} department to follow company naming convention")
            break
        elif department == "Accounting" or "accounting" == department:
            print(f"We can always rely on {department} department to follow company naming convention")
            break
        elif department == "FinOps" or "finOps" == department:
            print(f"We can always rely on {department} department to follow company naming convention")
            break
    else:
        return ("Error: In order to use this generator, you enter the name correctly. "
                "Example: Marketing, Accounting, FinOps")
        exit()


def no_negative(required_ec2):
    if required_ec2 < 0:
        print("Please enter a positive number: ")
    elif required_ec2 > 0:
        print(f"Creating {required_ec2} unique EC2 Instance Names")


department_name = input("Enter Department: Marketing, Accounting, FinOps: ")
number_of_ec2 = int(input("How many EC2 instances do you require?\n"))
while number_of_ec2 == "exit":
    validate_dept_name(department_name)
    no_negative(number_of_ec2)
    for _ in range(1, number_of_ec2 + 1):
        unique_name = department_name
        EC2_unique_name = unique_name + "-" + string_generator()
        print("Your EC2 Instance's unique name is : ", EC2_unique_name)
    else:
        exit()