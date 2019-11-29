##############################################################
# This a app to convert insulin units based on caloric grams.
# Author Joseph Nadeau
# Date 11/25/2019
###############################################################

import os
os.system('clear')

insulin_units = 0
carb_grams = 0
round_insulin_units = 0

print("  ********************************")
print("  *                              *")
print("  *  Carb Grams to Insulin Unit  *")
print("  *                              *")
print("  ********************************")
print("")

carb_grams = float(input("\tEnter carb grams.\n\n\t\t"))

print("")

blood_sugar = int(input("\tEnter blood sugar.\n\n\t\t"))
if(blood_sugar >= 181) and (blood_sugar <= 240):
    blood_sugar = insulin_units + 1
    

elif(blood_sugar >= 241) and (blood_sugar <= 320):
    blood_sugar = insulin_units + 2
    

else:
    (blood_sugar <= 181)
    blood_sugar = insulin_units + 0
    

print("")
insulin_units = carb_grams/15
print("  " + str(carb_grams) + " carb grams = " + str(round(insulin_units, 2))
 + " Insulin Units with adjustments of " + str(blood_sugar) + " Insulin units\n")
