li = [12,34,23,53,5]
total=0
for i in range(0,len(li)):
    total+=li[i]
   
average= total/len(li)

print(average)
print(len(li))

#another way to find average best practice
average1= sum(li)/len(li)
print(average1)
