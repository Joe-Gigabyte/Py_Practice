# This is a program to convert kilos to pounds.

import os
os.system('clear') # Use the OS system to clear the screen when this program runs.

kilo_pounds = 0 # Instantiate varible.

print("") # Add a line for aesthetics.

print("************************************") # A liitle bling.

user_input = float(input("Enter kilos\n")) # Prompt user for input.

kilo_pounds = user_input * 2.2 # Assigned the users input * 2.2 to var.

print("************************************")

print(str(user_input) + " kilos = " + str(kilo_pounds) + "pounds") # Print the converted user_input to a string and
# concantate with the conversion var.
