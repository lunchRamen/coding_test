import sys


input=sys.stdin.readline

n=int(input())

A=[]
B=[]
C=[]
D=[]

for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A.sort()
B.sort()
C.sort()
D.sort()

"""
a+b+c+d = 0인 경우를 찾는다.
(a+b) + (c+d) = 0인 경우를 찾는다.
a+b = -(c+d)인 경우를 찾는다.

그러면 4000*4000은 시간초과가 안나서 성공한다.

크게보면, dp문제 (큰 문제를 작게 쪼개서 해결했으니.)
또한, 시간복잡도를 낮추는 방법은 이분탐색 혹은 딕셔너리가 주로 쓰인다.
"""

dic_ab=dict()

for numA in A:
    for numB in B:
        if numA+numB in dic_ab:
            dic_ab[numA+numB]+=1
        else:
            dic_ab[numA+numB]=1
answer=0
for numC in C:
    for numD in D:
        if -(numC+numD) in dic_ab:
            answer+=dic_ab[-(numC+numD)]

print(answer)

