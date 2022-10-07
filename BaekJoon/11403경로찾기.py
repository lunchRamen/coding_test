import sys
import bisect
from collections import deque,defaultdict

input = sys.stdin.readline
INF = sys.maxsize


"""
floyd -warshall

-> 중간다리 노드를 꼈을때 해당 다리를 통해서 가는게 가중치가 더 낮다면 -> 원래 노드 가는 길의 가중치를 업데이트
여기서는 방문 가능여부만 따지면 되기때문에 더 간단하다.
"""


n=int(input())


arr = [list(map(int,input().split())) for _ in range(n)]


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][k] and arr[k][j]:
                    arr[i][j]=1
floyd()

for i in arr:
    print(*i)
