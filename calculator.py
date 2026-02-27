num1= int(input("Enter number1:"))
num2= int(input("Enter number2:"))
op=input("Etner Operation +,-,*,%:")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="%":
    print(num1%num2)
else:
    print("Invalid Operation...")