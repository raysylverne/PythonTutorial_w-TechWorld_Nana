calculation_to_units = 24
name_of_unit = "hours"
def days_to_units(num_of_days):
    print(num_of_days > 0)
    if num_of_days > 0:     # this is a conditional that cna be true or false
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "Please provide positive number for the conversion to work!"


user_input = input("Hey there, enter a number of days and I will convert it to hours: ")

calculated_value = days_to_units(int(user_input))
print(calculated_value)



''' NOTES
This will focus on restriction and validation of user input that logically doesn't make sense, could crash our program  
or could be a security risk. 
Line 5: Is the user input a positive number. Note: You have to indent the "return statement" so that it is evaluated by 
the "if statement" Or it will error out
Line 7: If user provides a negative # the else statement will return output that provides guidance
line 13: By nesting a function within a function days_to_units(int(user_input)) we've alleviated the need for the 
user_input_number variable
L 13: The Return value of the inner function is the input value for the outer function "days_to_units(int(user_input))"

'''

''' Expressions that evaluate to either true or false
Equals:  a == b, Not Equals: a != b,less than < , greater than >, less than or equal <=,  greater than or equal >=

'''