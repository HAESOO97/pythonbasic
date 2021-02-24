##내장함수
#sum()
result = sum([1,2,3,4,5])
print(result)
#min
result = min(7,3,5,2)
print(result)
#max
result = max(7,3,5,2)
print(result)
#eval
result = eval("(3+5)*7")
print(result)
#sorted
result = sorted([9,1,8,5,4]) ##오름차순으로 정렬
print(result)
result = sorted([9,1,8,5,4],reverse=True) #내림차순으로 정렬
print(result)

result = sorted([('홍길동',35),('이순신',75),('아무개',50)],key = lambda x:x[1], reverse=True)
print(result)

##iterable 객체(리스트, 튜플, 사전자료형)은 sort()함수 내장
data = [9,1,8,5,4]
data.sort()
print(data)

##itertools
#반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
#permutations(순열) : r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 계산
from itertools import permutations
data = ['A','B','C'] 
result = list(permutations(data,3))
print(result)
#combinations(조합) : r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data, 2))
print(result)

#poduct : permutations와 같지만 원소를 중복하여 뽑는다.
from itertools import product

data = ['A','B','C']
result = list(product(data,repeat=2))
print(result)

#combinations_with_replacement : combinations와 같지만 원소를 중복해서 뽑는다.

from itertools import combinations_with_replacement
data=['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)

##p
