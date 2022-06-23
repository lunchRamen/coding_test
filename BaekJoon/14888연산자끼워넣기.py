from itertools import combinations, permutations
import sys

input=sys.stdin.readline

n=int(input())

arr=list(map(int,input().split()))

plus,minus,multiple,divide=map(int,input().split())

minNum=1000000001
maxNum=-1000000001

sign_arr=[]

for _ in range(plus):
    sign_arr.append('+')
for _ in range(minus):
    sign_arr.append('-')
for _ in range(multiple):
    sign_arr.append("*")
for _ in range(divide):
    sign_arr.append("/")

for temp in permutations(sign_arr,n-1):
    tempSum=arr[0]
    for i in range(len(temp)):
        if temp[i]=='+':
            tempSum=tempSum+arr[i+1]
        elif temp[i]=='-':
            tempSum-=arr[i+1]
        elif temp[i]=='*':
            tempSum*=arr[i+1]
        else:
            if tempSum<0:
                tempSum=abs(tempSum)
                tempSum=tempSum//arr[i+1]
                tempSum=-tempSum
            else:
                tempSum=tempSum//arr[i+1]
    if tempSum>maxNum:
        maxNum=tempSum
    if tempSum<minNum:
        minNum=tempSum

print(maxNum)
print(minNum)