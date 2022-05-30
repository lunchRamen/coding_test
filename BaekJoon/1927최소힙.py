import sys
import heapq

input=sys.stdin.readline

n=int(input())

arr=[]

"""
파이썬의 Heapq는 기본적으로 min heap. 만약 maxheap을 하고싶다면, (-value,value)로
우선순위를 역으로 계산해 넣으면 된다.

굳이 heapq.heapify를 안해도, 모든 push,pop연산에 heapq로 연산을하면, 배열이 알아서 
heap자료구조로 변한다.

heap이 등장한 배경은, 컴퓨터구조,운영체제에서 우선순위 큐를 효율적으로 구현할 수 있는 것을
따지다가 나옴. 최대/최소값에 대한 삽입,삭제가 O(logN)으로 해결 됨.

또한, 트리구조로 이루어져있으므로, 최대 최소값에 대한 비교 연산으로 인덱스가 넘어가는 과정이
BST와 동일하다. 자식노드가 i면 부모노드는 //2 부모노드에서 자식노드갈때는 왼쪽이면 i*2 오른쪽이면 i*2+1

"""

for _ in range(n):
    num=int(input())
    if num==0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr,num)
