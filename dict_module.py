'''
Created two files dict_module.py and dict_helper.py in order to practice using modules. The code in dict_module.py
came from dictionarydatatypes.py
A module is a python file that contains funtions and variables that can be used by another python file within your
project. Essentially any python file within your file can become a module. The idea is that you can structure your
program using modules making your project modular. We will create our own module in the dict_helper.py file, and we're
going to reference in  dict_module.py.
'''

# END GOAL#
# 1- In dict_module.py I only want the code that starts the program.
# 2- Move and group all the functions, and logic in the dict_helper.py file
# 3- Use Modules to connect the two files


''' 
#There are two ways to connect two files the first way shown here brings the entire file over using the following
#syntax import <filename>  can be seen below you can also change the way a file is referenced within another file 
by giving it something like an alias with the following syntax "import helper as h"

import dict_helper

user_input = ""
while user_input != "exit":
    user_input = input(dict_helper.user_input_message) #dict_helper. was referenced here
    days_and_unit = user_input.split(':')
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    dict_helper.validate_and_execute(days_and_unit_dictionary) #dict_helper. was referenced here
'''

# The second way to connect tow files involves only brininging over select functions and variables instead of the
# entire file see below for syntax


from dict_helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(':')
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)


'''
The difference between  import helper and from helper import * <-Means Import everything
On the surface these appear to do the same thing, import the contents of an entire file into another 
The key difference is in the syntax that you have to use with each 

-When using the import <filename> statement you have to reference the name of the module every time you have to access 
something from that module

With the "from import" statement you list the functions or variables you want to use after the statement and use them as 
needed where you require them without having to reference the module they came from at every location. 

It comes down to a matter of preference. The situation may dictate which makes more sense but for now I find the 
"from import" statement to have a cleaner look out of the two. 
'''