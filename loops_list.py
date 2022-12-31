# for loop is used for iterating over a sequence (like a list)

calculation_to_units = 24
name_of_unit = "hours"
def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a positive number")
    except ValueError:
        print("Your input is not a number don't crash the program")


user_input = " "
while user_input != "exit":
    user_input = input("Heyjthere, enter a number of days as a comma separated list  and I will convert it to hours: ")
    for num_of_days_element in user_input.split(','):
        validate_and_execute()


'''
user_input.split() is a function that will take user input as a parameter and will give us a list data type
'''

