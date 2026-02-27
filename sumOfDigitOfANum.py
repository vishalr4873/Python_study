number = int(input("Enter number: "))
number = abs(number)

sumOfDigitOfNum = 0 

while number>0:
    lastDigit= number%10
    sumOfDigitOfNum = sumOfDigitOfNum + lastDigit
    number //= 10

print(sumOfDigitOfNum)