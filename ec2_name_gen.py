
'''
Finished EC2 name gen, now I want to create a while loop that alleviates the need to re-run the app every time its
needed. I also want to move all the logic to a sep module that will be call upon
'''
import sys
from ec2_name_gen_helper import no_negative, validate_dept_name, uuid4_generator


department_name = ""
number_of_ec2 = ""
while True:

    department_valid = False
    while not department_valid:
        department_name = input("Enter Department: Marketing, Accounting, FinOps (or type exit): ")
        department_valid = validate_dept_name(department_name)
        if department_name == 'exit':
            sys.exit()

    number_of_ec2 = int(input("How many EC2 instances do you require?: "))
    no_negative(number_of_ec2)
    for _ in range(1, number_of_ec2 + 1):
        unique_name = department_name
        EC2_unique_name = unique_name + "-" + uuid4_generator()
        print("Your EC2 Instance's unique name is: ", EC2_unique_name)
    more_instances = input("Do you need additional unique EC2 instances names created(Y/N): ")
    if more_instances == "Y" or "y" == more_instances: # exit if user no longer requires the program to run
        print("-----------------------------------------------------------------------------------")
        print("")
        continue # if true -> continue while loop
    else: # if false -> break
        sys.exit()


