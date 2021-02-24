##collections
#deque-popleft() : 첫번째 원소 제거
#     -pop() : 마지막 원소 제거
#     -appendleft(x) : 첫번째 인덱스에 원소 x삽입
#     -append(x) : 마지막 인덱스에 원소 x 삽입

from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

#Counter : 등장횟수를 세는 기능 제공

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

##math
#factorial(x) = x!
#sqrt(x) = x의 제곱근
#gcd(a,b) : a,b의 최대 공약수

import math

print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14))
print(math.pi)
print(math.e)