# This is a program to accept user input and convert inches to feet.
# Author - Joseph Nadeau
# Date - 11/24/2019
#################################################################

import os
os.system('clear') #Clear the console everytime it runs.

num = 1 # Number varible
footcount = 0 # feet varible
inches = 0 # Inches varible

# Prompting user for input.
user_input = int(input("Enter inches to find feet.\n"))

# While loop to iterate through users value.
while (num <= user_input):
    if (num % 12 == 0):
        footcount += 1
        print(str(num) + " inches =  " + str(footcount) + " feet")

        inches = num - user_input  # math operation to determine inches.

    num += 1
print(str(user_input) + " inches " + "= " + str(footcount) + " feet " + str(inches) + " inches")