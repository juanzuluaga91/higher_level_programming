#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = -4205
ld = number % 10
if number < 0:
    ld *= -1
if ld > 5:
    result = 'and is greater than 5'
elif ld < 6 and ld != 0:
    result = 'and is less than 6 and not 0'
else:
    result = 'and is 0'
print('The last digit of', '{:d}'.format(number), 'is', '{:d}'.format(ld), result)
