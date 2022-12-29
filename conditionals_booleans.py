# if statements, elif statements, else statements
'''
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number >0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
    else:
        print("Your input is not a number don't crash the program")

user_input = input("Hey there, enter a number of days and I will convert it to hours: ")
validate_and_execute()
'''


''' NOTES
Now we want to focus on restriction and validation of user input that logically doesn't make sense, could crash our 
program  or could be a security risk. 
Line 5: Is the user input a positive number. Note: You have to indent the "return statement" so that it is evaluated by 
the "if statement" Or it will error out
Line 7: If user provides a negative # the else statement will return output that provides guidance
Line 8: If you need to check user input against multiple conditions use the "elif:" statement for any subsequent 
Conditions after the first. You can have multiple "elif:" statements between the "if" statement and the else statement
Line 13: Added and "if statement" to validate that the user input is an integer "if user_input.isdigit():"
This also rejects user_input that is a string, float, and negative #. 
line 14: By nesting a function within a function days_to_units(int(user_input)) we've alleviated the need for the 
user_input_number variable
L 14: The Return value of the inner function is the input value for the outer function "days_to_units(int(user_input))"


The WorkFlow Breakdown : User Input is accepted as a string> The int() function converts the string to and integer and passes the 
Value into the days_to_units function > Before executing the function our if statement evaluates if it is true or false
If true the function returns the calculated string > If false our else statement return the other string. 
'''

''' Expressions that evaluate to either true or false
Equals:  a == b, Not Equals: a != b,less than < , greater than >, less than or equal <=,  greater than or equal >=
'''

# Error Handling with Try/Except
# If statements will only catch the errors we think of and prepare a condition for but if a user passed something we
# haven't thought of that could crash the program. The try statement specifies exception handlers and/or cleanup code
# for a group of statements. Try statement lets you "test" a block of code for errors. try: statements are useful
# if in a situation where you can't validate input using if statements

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
    except ValueError:  #Add the type of error you want to catch on this line after excpet. You can also leave it blank
        #if you want to catch any error not just the one you specified.
        print("Your input is not a number don't crash the program")

user_input = input("Hey there, enter a number of days and I will convert it to hours: ")
validate_and_execute()



# Saved this version since it represents a simplified version of the syntax. Specifically the conversion of user_input
#from string to int() on line 90
'''calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    if user_input.isdigit():
        calculated_value = days_to_units(int(user_input))
        if int(user_input) > 0:  # this is a conditional that cna be true or false
            print(calculated_value)
    else:
        print("Your input is not a number don't crash the program")

user_input = input("Hey there, enter a number of days and I will convert it to hours: ")
validate_and_execute()
'''