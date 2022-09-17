#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
     new_list = []
    for i in range(0, list_length):
        divides = 0
        try:
            divides = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divides = 0
        except ZeroDivisionError:
            print("division by 0")
            divides = 0
        except IndexError:
            print("out of range")
        finally:
            new_list.append(divides)
    return new_list
