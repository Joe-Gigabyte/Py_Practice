##############################################################
# This a app to convert insulin units based on carbs in grams.
# Author Joseph Nadeau
# Date 11/25/2019
###############################################################

import os
os.system('clear')

insulin_units = 0
carb_grams = 0
round_insulin_units = 0

print("  ********************************")
print("  *           Jadyn's            *")
print("  *  Carb Grams to Insulin Unit  *")
print("  *        Conversion App        *")
print("  ********************************")
print("")

carb_grams = float(input("\tEnter carb grams.\n\n\t\t"))
insulin_units = carb_grams/15

print("")

blood_sugar = int(input("\tEnter blood sugar.\n\n\t\t"))
if(blood_sugar >= 181) and (blood_sugar <= 240):
    insulin_adj = insulin_units + 1
    

elif(blood_sugar >= 241) and (blood_sugar <= 320):
    insulin_adj = insulin_units + 2

elif(blood_sugar >= 321):
    insulin_adj = insulin_units + 3
    

else:
    (blood_sugar <= 181)
    insulin_adj = insulin_units + 0
    

print("")
print("\tCarb Grams was " + str(carb_grams))

print("")
print("\tBlood Sugar was " + str(blood_sugar))

print("")
print("\tInsulin Units needed " + str(round(insulin_units, 2)))
print("")

print("")
print("\tInsulin with Adjustment " + str(round(insulin_adj, 2)))
print("")

print("  ***********************************")
print("\tBlood Sugar Adjustment Chart")
print("")
print("\tLow\tHigh\tAdjustment")
print("\t0\t180\t0")
print("\t181\t240\t1")
print("\t241\t320\t2")
print("\t321\t& Up\t3")
print("  ***********************************")




#print("  " + str(carb_grams) + " carb grams = " + str(round(insulin_units, 2))
# + " Insulin Units with adjustments of " + str(blood_sugar) + " Insulin units\n")
