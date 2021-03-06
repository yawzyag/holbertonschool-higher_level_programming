#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            num = 0
            print("division by 0")
        finally:
            new_list.append(num)
    return new_list
