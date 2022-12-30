# while Loops
# A while loop will run a piece of code while a condition is True. It will keep executing the desired set of code
# statements until that condition is no longer True.
#  A while loop will always first check the condition before running.
# If the condition evaluates to True then the loop will run the code within the loop's body.


calculation_to_units = 24
name_of_unit = "hours"
def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a positive number")
    except ValueError:
        print("Your input is not a number don't crash the program")


while True:
    user_input = input("Hey there, enter a number of days and I will convert it to hours: ")
    validate_and_execute()