calculation_to_units = 24
name_of_unit = "hours"
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


user_input = input("Hey there, enter a number of days and I will convert it to hours: ")

user_input_number = int(user_input)
calculated_value = days_to_units(user_input_number)
print(calculated_value)



''' NOTES
This will focus on restriction and validation of user input that logically doesn't make sense, could crash our program  or could be a security risk. 
Line 4: Is the user input a positive number. Note: You have to indent the "return statement" so that it is evaluated by the "if statement" Or it will error out
'''

''' Expressions that evaluate to either true or false
Equals:  a == b, Not Equals: a != b,less than < , greater than >, less than or equal <=,  greater than or equal >=

'''