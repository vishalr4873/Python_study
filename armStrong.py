#armstrong number 153
number= int(input("Enter a number: "))

orginalNumber=number
result=0

while number>0:
    lastdigitsqr = (number%10)**3
    result = result+lastdigitsqr
    number= number//10
    
if orginalNumber== result:
    print("It is a armstrong number")
else:
    print("Not armStrong")
