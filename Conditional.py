# if else
import os
#import sys

name = input("What is your name: ")
age = input("Enter your age : ")
# CTRL+ALT+L to align
if not age.isnumeric():
    print("Invalid age")
    # terminate
    os._exit(0)
    # sys.exit()

if int(age) > 18:
    print(name + " is an adult")
else:
    print(name + " is a child")

    # list, booleans tuples, dictionary, loops
