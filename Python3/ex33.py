#!/bin/python3

# ex33: While Loops

def createNumbers(max, step):
    i = 0
    numbers = []
    while i < max:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    return numbers 

numbers = createNumbers(10, 2)

print("The number: ")

for num in numbers:
    print(num)
