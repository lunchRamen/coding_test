import sys

input=sys.stdin.readline

n,m=map(int,input().split())

arrN=[]
arrM=[]
cnt=0

for _ in range(n):
    arrN.append(input())

for _ in range(m):
    arrM.append(input())

for i in range(m):
    if arrM[i] in arrN:
        cnt+=1

print(cnt)
