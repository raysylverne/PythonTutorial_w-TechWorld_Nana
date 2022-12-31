import datetime


user_input = input("Enter your goal with a deadline seperated by a colon!\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

test = datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(test)




#python:1.7.2023