import sys
import bisect

def binary_search(array,target,start,end):
    try:
        if start>end:
            return 0
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            return binary_search(array,target,start,mid-1)
        else:
            return binary_search(array,target,mid+1,end)
    except: #예외로 벗어나는 인덱스에 대한 처리.
        return 0


input=sys.stdin.readline

n,m=map(int,input().split())

arrN=[]
arrM=[]

for _ in range(n):
    arrN.append(input().rstrip())
for _ in range(m):
    arrM.append(input().rstrip())
arrN.sort()
arrM.sort()

answer=[]
for i in range(len(arrN)):
    if binary_search(arrM,arrN[i],0,len(arrM)):
        answer.append(arrN[i])
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])