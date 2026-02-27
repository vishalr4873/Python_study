name = [23,43,23,53]
largest = name[0]


for i in range (1,len(name)):   
        if name[i]>largest:
                largest=name[i]

print(largest)

#next mathod
print(max(name))