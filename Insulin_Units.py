##############################################################
# This a app to convert insulin units based on caloric grams.
# Author Joseph Nadeau
# Date 11/25/2019
###############################################################

import os
os.system('clear')

insulin_units = 0
calories_grams = 0
round_insulin_units = 0

calories_grams = float(input("Enter calorie grams.\n"))

print("")

insulin_units = calories_grams/15
print(str(calories_grams) + " = " + str(insulin_units) + " units\n")

round_insulin_units = round(insulin_units)
print("Insulin units rounded to " + str(round_insulin_units))