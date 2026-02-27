number = int(input("Enter number: "))
count = 0

while number > 0:
    count += 1
    number //= 10

print(count)

#another way above give wrong output when number will be 0
number = int(input("Enter number: "))

if number == 0:
    count = 1
else:
    count = 0
    while number > 0:
        number //= 10
        count += 1

print(count)