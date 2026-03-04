li=[3,3,5,2,5,1,6]
li.sort()
print(li)

#list in descending order
newList = sorted(li,reverse=True)
print(newList)

#list in descendig order another way
#li.sort(reverse=true)

# numpy1.py

import numpy as np
li= []
for i in range(1,5):
    inp_put= int(input("Enter a number here: "))
    (li.append(inp_put))

print(type(np.array(li)))

#1D array
arr= np.array([23,43,32,43,134,4])
print(arr)

#2D array
arr= np.array([[23,43,32,43,134,4],[23,23,23,4,2,5]])
print(arr)
print(arr.ndim)

#ND array
arr= np.array([23,43,32,43,134,4],ndmin=10)
print(arr)