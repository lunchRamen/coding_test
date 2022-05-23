import sys
from collections import deque

input=sys.stdin.readline


t=int(input())

while t:
    functionStr=input()
    n=int(input().rstrip('\n'))
    arr=input()
    flag=False
    rev=0
    if n==0:
        arr=[]
    else:
        arr=arr[1:len(arr)-2].split(",")
        arr=deque(arr)
    
    for i in range(len(functionStr)):
        if functionStr[i]=="R":
            rev+=1
        if functionStr[i]=="D":
            if len(arr)==0:
                flag=True
                continue
            else:
                if rev%2==0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag:
        print("error")
    else:
        if rev%2==0:
            print("["+",".join(arr)+"]")
            # print(list(arr))
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")
            # print(list(arr))
    t-=1