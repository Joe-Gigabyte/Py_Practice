# This is a program to convert kilos to pounds.

import os
os.system('clear')

kilo_pounds = 0 # Instantiate varible
print("")
print("************************************")
user_input = float(input("Enter kilos\n")) # Prompt user for input.

kilo_pounds = user_input * 2.2

print("************************************")
print(str(user_input) + " kilos = " + str(kilo_pounds) + "pounds")

