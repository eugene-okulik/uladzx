numbers = range(1, 101)

numbers_llist = list(numbers)

for number in numbers:
    if int(number) % 3 == 0 and int(number) % 5 != 0:
        print("Fuzz")
    elif int(number) % 5 == 0 and int(number) % 3 != 0:
        print("Buzz")
    elif int(number) % 3 == 0 and int(number) % 5 == 0:
        print("FuzzBuzz")
    else:
        print(number)
