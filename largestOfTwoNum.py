number1 = int(input("Enter a number1 here: "))
number2 = int(input("Enter a number2 here: "))

largestOfTwo= max(number1,number2)

print(f"{largestOfTwo} is largest")

#another way
if number1>number2:
    print(f"{number1} is largest number")
else:
    print(f"{number2} if largest")