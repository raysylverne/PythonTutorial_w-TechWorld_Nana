from uuid import uuid4


def validate_dept_name(department):
    if department == "Marketing" or department == "marketing":
        print(f"We can always rely on {department} department to follow company naming convention")
        return True
    elif department == "Accounting" or "accounting" == department:
        print(f"We can always rely on {department} department to follow company naming convention")
        return True
    elif department == "FinOps" or "finOps" == department:
        print(f"We can always rely on {department} department to follow company naming convention")
        return True
    elif department != 'exit':
        print("Error: In order to use this generator, you enter the name correctly. "
                "Example: Marketing, Accounting, FinOps")
        return False


def no_negative(required_ec2):
    if required_ec2 <= 0:
        print("Please enter a positive number: ")
    elif required_ec2 > 0:
        print("")
        print("--------------------------------")
        print(f"Creating {required_ec2} Unique EC2 Instance Names")
        print("--------------------------------")

def uuid4_generator():
    return str(uuid4())

