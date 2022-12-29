calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:     # this is a conditional that cna be true or false
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "Please provide positive number for the conversion tool to work!"


user_input = input("Hey there, enter a number of days and I will convert it to hours: ")
if user_input.isdigit():
    calculated_value = days_to_units(int(user_input))
    print(calculated_value)
else:
    print("Your input is not a number don't crash the program")

''' NOTES
Now we want to focus on restriction and validation of user input that logically doesn't make sense, could crash our 
program  or could be a security risk. 
Line 5: Is the user input a positive number. Note: You have to indent the "return statement" so that it is evaluated by 
the "if statement" Or it will error out
Line 7: If user provides a negative # the else statement will return output that provides guidance
Line 8: If you need to check user input against multiple conditions use the "elif" statement for any subsequent 
Conditions after the first. You can have multiple "elif" statements between the "if" statement and the else statement
line 13: By nesting a function within a function days_to_units(int(user_input)) we've alleviated the need for the 
user_input_number variable
L 13: The Return value of the inner function is the input value for the outer function "days_to_units(int(user_input))"

The WorkFlow Breakdown : User Input is accepted as a string> The int() function converts the string to and integer and passes the 
Value into the days_to_units function > Before executing the function our if statement evaluates if it is true or false
If true the function returns the calculated string > If false our else statement return the other string. 
'''

''' Expressions that evaluate to either true or false
Equals:  a == b, Not Equals: a != b,less than < , greater than >, less than or equal <=,  greater than or equal >=
'''