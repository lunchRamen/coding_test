from itertools import combinations
import sys

input=sys.stdin.readline


n=int(input())  #n번째 감소하는 수

arr=[]

for i in range(1,11):
    for temp in combinations(range(0,10),i):
        temp=list(temp)
        temp.sort(reverse=True)
        arr.append(int("".join(map(str,temp))))

arr.sort()

try:
    print(arr[n])
except:
    print(-1)
