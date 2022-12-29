calculation_to_units = 24
name_of_unit = "hours"

# return statement is a special statement that you can use inside a function or method to
# send the function's result back to the caller. In this case the results of the function is being
# passed to the calculated_value variable which then can be used with the print function to display outcome

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

# input() value by default is always treated as a string. In this scenario if you don't use the int() function
# it will simply display the inputted number 24 times "1010101" instead multiplying by 24. See final comments for
# full explanation (lines25-29)

user_input = input("Hey there, enter a number of days and I will convert it to hours: \n")

# Encapsulating the variable user_input in the int is called casting.
# The int in python is a built-in method that converts a string or a number into an integer


user_input_number = int(user_input)
calculated_value = days_to_units(user_input_number)
print(calculated_value)

'''Realized that function wasn't working due to the days_to_units function treating num_
of_days as a string insead of an integer. Created the user_input_number variable that converts the user_input 
to an integer by calling the int() function. Now when the calculated_value variable calls the 
"days_to_units(user_input_number)" the code works since its treating num_of_days aka 
user_input_number as an integer instead of a string
'''
