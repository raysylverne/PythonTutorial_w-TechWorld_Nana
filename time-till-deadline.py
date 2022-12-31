import datetime

# Created user input statement and assign it to a variable
user_input = input("Enter your goal with a deadline separated by a colon!\n")

# Use the split(":") function to add the user inputs to a list separated by a colon and assign a variable
input_list = user_input.split(":")

# Index the goals and deadline parameters separately and assign each to a variable
goal = input_list[0]
deadline = input_list[1]

# Use the datetime.strptime(deadline, "%m.%d.%Y") function to convert deadline string to a DATE data type
# The order of "%m.%d.%Y" will dictate how your date is formatted
deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%Y")

# call the .today() function to get today's date
today_date = datetime.datetime.today()

# calculate how many days from now until the deadline
days_till_deadline = (deadline_date - today_date)

# Use the completed logic to print a message back to the user
print(f"Dear user! The time remaining for your goal: {goal} is {days_till_deadline.days} days "
      f"which is {int(days_till_deadline.total_seconds() / 60 / 60)} hour ")

# Note that when you want to pass a variable within a string you have to place an (f) at the start of the string and
# encapsulate any variable you want to pass within curly brackets {} as seen above

# Python:1.7.2023
# Python:2.7.2023


