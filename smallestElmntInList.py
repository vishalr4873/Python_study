#smallestEleInList.py

li=[9,0,1,2,3,5]
smallestEle=li[0]
for i in range(0,len(li)):
    if li[i]<smallestEle:
        smallestEle=li[i]

print(smallestEle)

#anthor way and best solution
smalllllest= min(li)
print(smalllllest)

name= "vishal"
print(name[::-1])