import sys
import bisect
from collections import deque,defaultdict

input = sys.stdin.readline
INF = sys.maxsize

# sys.setrecursionlimit(10**5)
"""
모든 정점에서 모든정점의 최소 가중치값 -> 플로이드-워셜

여기서 간과한점 두가지.
min값을 따질거면, 조건의 최대치를 배열에 넣어놓자.(초보적인 실수)
i->i로 가는거면, 굳이 갈 필요가 없다(생각을 해보면 답이 나옴)

또 헷갈렸던게, 단순히 가중치가 100,000이하라고 해서, 10만으로 arr값을 채워넣을게 아니라,
왔다 갔다 하면서 10만이 계속 더해질걸 생각해서 그냥 맘편히 min값 따질때는
sys.maxsize를 쓰도록 하자.
"""


n=int(input())

arr=[[INF for _ in range(n)] for _ in range(n)]

m = int(input())

for _ in range(m):
    x,y,w = map(int,input().split())
    
    num = min(w,arr[x-1][y-1])
    arr[x-1][y-1]=num


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j and arr[i][k]+arr[k][j]<arr[i][j]:
                arr[i][j]=arr[i][k]+arr[k][j]

for i in range(n):
    for j in range(n):
        if i==j:
            arr[i][j]=0
        if arr[i][j]==INF:
            arr[i][j]=0

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
