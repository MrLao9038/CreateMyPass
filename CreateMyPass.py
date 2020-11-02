#!/usr/bin/env python3        #Select interpreter for BASH

import random                 #Module for generating pseudo-random number

print("Generate Passwords For Me")
print("                                                  ")

print("--------------------------------------------------")     #Ascii Art
print("eeeee eeeee eeeee eeeee e  e  e 8eee8 eeeee  eeeee")
print("8   8 8   8 88    88    8  8  8 8   8 8   8  8   8")
print("8eee8 8eee8 8eeee 8eeee 8  8  8 8   8 8eee8e 8e  8")
print("88    8   8    88    88 8  8  8 8   8 8    8 88  8")
print("88    8   8 8ee88 8ee88 8ee8ee8 8eee8 8    8 88ee8")
print("--------------------------------------------------")

print("                                                  ")

print("Here Are The Passwords")
print("                                                  ")

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            #List of letters, numbers, and special characters for password
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
special_characters = "@%+|?!#$^?:,(){}[]~_-./\\"

upper, lower, nums, chars = True, True, True, True          #Boolean statements to choose which items on list to be included
                                                            #in password generating process
                    
all = ""      #Empty string to store our random generated password

if upper:                                                   #Based on boolean statement, we can select what will be included
    all += uppercase_letters                                #password
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if chars:
    all += special_characters

length = 20             #We can dictate the length of password, the longer the better
amount = 10             #We can dictate how many password to generate at a given time 

for ele in range(amount):
    password = "".join(random.sample(all, length))          #join all the random list of iterable into one string, based on the
    print(password)                                         #length we specify
