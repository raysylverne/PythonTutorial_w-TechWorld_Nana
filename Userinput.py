calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

# input() value by default is always treated as a string. In this scenario if you don't
# it will simply display the inputted number 24 times "1010101" instead multiplying by 24
user_input = input("Hey there, enter a number of days and I will convert it to hours: \n")
# Encapsulating the variable user_input in the int is called casting.
# The int in python is a built-in method that converts a string or a number into an integer
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)


'''return statement is a special statement that you can use inside a function or method to 
send the function's result back to the caller.'''
