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

''' 
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units(20)
days_to_units(20)
days_to_units(40)
'''

# How to pass multiple input variables to a function

calculation_to_units = 24
name_of_unit = "hours"

# Add your variable within the rounded brackets and separate with a comma
# Add the newly created variable within your function (custom_message)
'''
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(20, "Awesome")
days_to_units(30, "Looks Great")
days_to_units(40, "Job Well Done!")
'''

# Variable Scope and Function
# A variable is only available from inside the region it is created
# -Global Variable = variable available from within any scope
# -Local Variable = variables created inside a function and only available to that function

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


# Local Variables like num_of_days are only availble within the function is was created
# Hence the name local. If you try to use it outside of that function you will get and error
# You would have to redefine the variable in the new function before you could call on it

def scope_check():
    print(name_of_unit)    #This area is known as the function body
    print(num_of_days)     #This area is known as the function body

scope_check()