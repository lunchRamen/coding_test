import sys

input=sys.stdin.readline

"""
한 단계에 k-1 k k+1만큼 이동 가능.
1단계=1만큼 이동
2단계=0 1 2만큼 이동
3단계=0 1 2 / 1 2 3 / 2 3 4 만큼 이동 가능(각각 0 1 2 를 선택했을 경우)
... 이런식으로 나아감.
마지막엔 항상 +1만큼만.

start=x end=y에서
최단 경로로 가려면 몇번 이동해야하는지.

일단, y-1해줌
그다음 cnt를 구한값에 +1을 해줌.

ex)
0 3 = 1+1+1=3
1 5 =1+2+1=3
45 50= 1+2+1+1+4

y-x=temp로 두고
1+x+x+x+...+1 이런 형태로 진행 될 예정.

"""

t=int(input())


for i in range(t):
    x,y=map(int,input().split())

    d=y-x
    n=1
    while True:
        if d>n*(n+1):
            n+=1
        else:
            break
    if d<=n*n:
        print(2*n-1)
    else:
        print(2*n)