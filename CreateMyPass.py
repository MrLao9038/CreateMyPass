#!/usr/bin/env python3

import random

print("Generate Passwords For Me")
print("                                                  ")

print("--------------------------------------------------")
print("eeeee eeeee eeeee eeeee e  e  e 8eee8 eeeee  eeeee")
print("8   8 8   8 88    88    8  8  8 8   8 8   8  8   8")
print("8eee8 8eee8 8eeee 8eeee 8  8  8 8   8 8eee8e 8e  8")
print("88    8   8    88    88 8  8  8 8   8 8    8 88  8")
print("88    8   8 8ee88 8ee88 8ee8ee8 8eee8 8    8 88ee8")
print("--------------------------------------------------")

print("                                                  ")

print("Here Are The Passwords")
print("                                                  ")

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
special_characters = "@%+|?!#$^?:,(){}[]~_-./\\"

upper, lower, nums, chars = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if chars:
    all += special_characters

length = 20
amount = 10

for ele in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
