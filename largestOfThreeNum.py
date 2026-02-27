number1 = int(input("Enter a number1 here: "))
number2 = int(input("Enter a number2 here: "))
number3 = int(input("Enter a number3 here: "))

if number1>=number2 and number1>=number3:
    print(f"{number1} is largest number")
elif number2>=number3 and number2>=number1:
    print(f"{number2} is largest number")
else:
    print(f"{number3} if largest")


#another way
largest= max(number1,number2,number3)
print(f"{largest} is largest")