import sys
from bisect import bisect_left,bisect_right


input=sys.stdin.readline


n=int(input())
arrN=list(map(int,input().split()))
m=int(input())
arrM=list(map(int,input().split()))

arrN.sort()

answer=[]
for i in range(len(arrM)):
    answer.append(bisect_right(arrN,arrM[i])-bisect_left(arrN,arrM[i]))
    #만약 arrN에 arrM[i]와 매핑되는 값이 없다면, left,right값이 같아서 0이 나오게 된다.

for i in range(len(answer)):
    print(answer[i],end=' ')

