# Introducing the use of functions
'''
Functions are defined using the "def" keyword
Functions are like variables except an entire block of code can be placed into a function
'''

''' 
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units():
    print(f"20 Days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")
    
day_to_units()
'''

# A function contains a Block of code which only runs when it is called
# The round () brackets at the end of the string lets python know we are calling a function



               # Adding Input Parameters to a Function
# Information can be passed into functions as parameters
# Parameters are also called arguments (input)


calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


days_to_units(20, "Awesome!")
days_to_units(30, "Looks Good!")

