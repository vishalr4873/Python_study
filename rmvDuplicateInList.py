
# rmvDuplicateInList.py

li = [1,4,5,1,9,0,0,3,1,5]

li=list(set(li))
print(li)


#anthoer and best solution 
li = list(dict.fromkeys(li))
print(li)


#using loop

li = [1,4,5,1,9,0,0,3,1,5]
unique = []

for num in li:
    if num not in unique:
        unique.append(num)

print(unique)
