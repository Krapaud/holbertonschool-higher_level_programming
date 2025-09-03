#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        result = a
        for i in range(b - 1):
            result *= a
        return result
    else:
        return 1 / pow(a, -b)
