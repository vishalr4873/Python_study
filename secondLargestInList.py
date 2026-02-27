name = [23,43,23,53,123,123]
largest = name[0]
seconLargest=name[0]


for i in range (1,len(name)):   
        if name[i]>largest:
                seconLargest=largest
                largest=name[i]
        elif name[i]>seconLargest and name[i]!=largest:
                seconLargest=name[i]
            
print(seconLargest)
