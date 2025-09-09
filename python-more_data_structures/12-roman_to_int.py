#!/usr/bin/python3
def roman_to_int(roman_string):
    valeur = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    sum = 0
    prev = 0
    for char in reversed(roman_string):
        current = valeur.get(char, 0)
        if current < prev:
            sum -= current
        else:
            sum += current
        prev = current
    return sum
