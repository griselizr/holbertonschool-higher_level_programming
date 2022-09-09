#!/usr/bin/python3
for numbers in range(0, 9):
    for num in range(numbers + 1, 10):
        if numbers == 8 and num == 9:
            print("{}{}".format(numbers, num))
        else:
            print("{}{}".format(numbers, numb), end=", ")
