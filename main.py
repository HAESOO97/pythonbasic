##heapq
import heapq
def heapsort(iterable):
  h=[]
  result=[]
  #모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,value)
  #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

##최대힙
import heapq
def heapsort(iterable):
  h=[]
  result=[]
  for value in iterable:
    heapq.heappush(h,-value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

##bisect
#bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
#bisect_right(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right
a=[1,2,4,4,8]
x=4
print(bisect_left(a,x))
print(bisect_right(a,x))

#count_by_range(a, left_value, right_value)
# : left_value<=x<=right_value인 원소 x의 개수

from bisect import bisect_left,bisect_right

def count_by_range(a,left_value,right_value):
  right_index = bisect_right(a,right_value)
  left_index = bisect_left(a, left_value)
  return right_index-left_index
#리스트 선언
a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))