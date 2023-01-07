n = ""
while n != "exit":
    n = int(input("provide a number: ").strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 7, 2): # why does this print not weird even though my range is set to stop at 6
        print("Not Weird")
    elif n % 2 == 0 and n > 6 and n <= 20:
        print("Weird1")
    elif n % 2 == 0 and n > 20:
        print("Weird2")
    else:
        pass
