#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    num = 0
    for i in range(lenght):
        if i == 0 or my_list[i] > num:
            num = my_list[i]
    return num
