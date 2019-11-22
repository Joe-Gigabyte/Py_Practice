# Author is John Elder for Codemy.com
# Fizzbuzz
# 11/22/2019

num = 1 # varible to count 1 to 100
fizzbuzzcount = 0 # Counter Varible
fizzcount = 0
buzzcount = 0

while (num <= 100):
    if (num % 3 == 0) and (num % 5 == 0): #Using modulus to get the numbers that 3 and 5 will divide into evenly.
        print(str(num) + ". Fizzbuzz!")
        fizzbuzzcount += 1

    elif (num % 3 == 0):
        print(str(num) + ". Fizz!")
        fizzcount += 1

    elif (num % 5 == 0):
        print (str(num) + ". Buzz!")
        buzzcount += 1

    else:
        print(str(num) + ".")

    num += 1

print("*******************************************")
print("Fizz\tBuzz\tFizzbuzz")
print(str(fizzcount) + "\t" + str(buzzcount) + "\t" + str(fizzbuzzcount))
print("*******************************************")