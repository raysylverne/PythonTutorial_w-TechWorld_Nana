import random

numbers = [0, 1, 2, 3, 4]

for number in numbers:
    print(number * number)

for i in range(len(numbers)):
    print(i, numbers[i])

for i in range(10):
    print(random.randint(0, 10))

number = random.randint(0, 10)
counter = 0

while (number != 7):
    counter += 1  # counter = counter + 1
    number = random.randint(0, 10)

print(number, counter)

# %%

number = random.randint(0, 10000)
counter = 0

while (number != 7):
    if (counter > 10000):
        break
    counter += 1  # counter = counter + 1
    number = random.randint(0, 10000)

print(number, counter)

# %%

number = random.randint(0, 10000)

for i in range(10000):
    if (number == 7):
        break
    number = random.randint(0, 10000)

print(number, i)

# %%

print(numbers)

if (2 in numbers):
    print("True")

# %%

# objects = [{"numbers": [random.randint(0, 10) for j in range(5)]} for i in range(10)]
# command is expanded below

objects = []

for i in range(10):
    nums = []
    for j in range(5):
        number = random.randint(0, 10)
        nums.append(number)

    dict_obj = {"numbers": nums}
    objects.append(dict_obj)

print(objects)

for i in range(len(objects)):
    if (2 in objects[i]['numbers']):
        print(i, "True")