number1 = int(input("Enter number1 "))
number2 = int(input("Enter number2 "))

gcd=1

for i in range(2,min(number1,number2)+1):
    if number1%i==0 and number2%i==0:
        gcd=i
        
print(gcd)