import numpy as np

x = [1, 2, 3]
y = np.array(x)
print(type(y))

print(y)

x = []
for i in range(1,6):
    user_input= int(input("Enter a number here: "))
    x.append(user_input)

print(np.array(x))
dim= np.ndim(x)
print(dim)

arr=[[2,3,4,5,6],[1,2,3,4,5]]
newArr= np.array(arr)
print(newArr)

arr1=[[[2,3,4,5,6],[1,2,3,4,5],[1,2,3,4,5]]]
newArr1= np.array(arr1)
print(newArr1)

arr=[2,3,4,5,6] 
newArr = np.array(arr, ndmin=10)
print(newArr)