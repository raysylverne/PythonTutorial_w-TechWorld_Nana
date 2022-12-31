'''
Currently the program takes the number of days that the user input and converts that to number of hours.
We added while and for loops to allow the user to call the program an unlimited number of times with up to and unlimited
number of request at a time so long as their separated by a comma. However, what if we wanted our users
to decide what units days should be converted to. Like what if we wanted to convert minutes instead of hours.
So instead of a providing a list the user will users to input the number of days and whether they want to convert to
seconds, minutes, or hours
'''


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60 } seconds"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a positive number")
    except ValueError:
        print("Your input is not a number don't crash the program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey there, enter a number of days and conversion unit.\n"
                       "Conversion unit can be seconds, minutes our hours.\n"
                       "Exp input (45:hours) Enter text here: ")
    days_and_unit = user_input.split(':')
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()


'''
When referencing items in a list in a different part of your code you identify that item in square [] using the index
value. However when referencing items in a dictionary you  still use square brackets but reference the "key" instead of
an index.  
Example:
my_list = ["20", "30", "50"]
print(my_list[2])
output >>> 50

my_dictionary = {"days": 20, "unit": "hours"}
print(my_dictionary["unit"])
output >>> hours
 '''

'''
#Breakdown of core Data Types within Python
message = "enter some value" #string
days = 20 #integer
price = 9.99 #float
valid_number = True #boolean
exit_input = False #boolean
list_of_days = [20, 40, 50, 100] #lists = [] are created using Square brackets
list_of_months = ["Jan", "Feb", "Mar", "April", "May"]  #list can hold numbersl or strings
set_of_days = {20, 40, 50, 100, } # sets = {} are very similar to list except it does not allow duplicate values
days_and_unit = {"days": 10, "unit": "hours"} #dictionary are created using a key-value pair wrapped in curly brackets
'''