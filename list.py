a=[1,2,3,4,5,6,7,8,9]
print(a)

print(a[4])

a=list()
print(a)
a=[]
print(a)

n=10
a=[0]*n
print(a)

a=[1,2,3,4,5,6,7,8,9]
print(a[-1])
print(a[-3])
a[3]=7
print(a)

print(a[1:4])

<리스트 컴프리헨션>
array=[i for i in range(20) if i%2==1]
print(array)

<일반적인 소스코드>
array =[]
for i in range(20):
  if i%2 == 1:
    array.append(i)
print(array)
