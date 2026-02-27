number = int(input("Enter number: "))
count=0
if number == 0:
    count=1
while number>0:
    number//= 10
    count= count+1

print(count)