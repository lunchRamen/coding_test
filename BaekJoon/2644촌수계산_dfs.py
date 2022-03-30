"""
문제풀이

주어진 두 idx를 통해
두 idx가 이어질때까지 몇번의 재귀호출이 이뤄졌는지.
->촌수를 구하는것과 동일한 동작.

person의 경우 2차원 배열
visit의 경우 1차원 배열 생성.

person의 경우
person[i]는 1번째와 부모-자식관계가 형성된 노드들.

그래서 a,b에 대해 서로 추가를 해줌(양방향이라서)
그 다음, dfs를 호출하는데,
탈출 조건은 재귀호출되는 start가 p2와 같은경우
이 경우 재귀호출 횟수인 cnt를 num에 할당하고 return

아니라면, 재귀가 진행되어야 하니까
person[start]에 대해서
i번째 idx는 제외하고,
방문한 idx도 제외하고,
i번째와 부모-자식 관계가 있는 모든 노드들을
방문 표시한 후, dfs(i,cnt+1)로 재귀호출함.
이렇게 되면, 촌수관계가 있는 i에 대해 다시 촌수관계를
따짐..무한반복
"""

import sys

input=sys.stdin.readline
num=-1
def dfs(start,cnt):
    global num
    if start==p2:
        num=cnt
        return

    for i in person[start]:
        if i==0:
            continue
        if visit[i]==1:
            continue
        visit[i]=1
        dfs(i,cnt+1)
    

n=int(input())

p1,p2=map(int,input().split())
m=int(input())

person=[[0] for _ in range(n+1)]
visit=[0 for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    person[a].append(b)
    person[b].append(a)

answer=dfs(p1,0)
print(num)