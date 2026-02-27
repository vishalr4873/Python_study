number = int(input("Enter number: "))
reverse = 0 
while number>0:
    lastDigit= number%10
    reverse = reverse*10 + lastDigit
    number //= 10

print(reverse)