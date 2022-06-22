import sys

input=sys.stdin.readline

n,m,b=map(int,input().split())

arr=[]
answer=sys.maxsize
answerFloor=0

for _ in range(n):
    temp=list(map(int,input().split()))
    arr.append(temp)

for floor in range(257):    #0~256까지 모든 땅의 높이 "전수조사"
    plus_floor,minus_floor=0,0 #모든 칸들을 돌려, 해당 층을 맞추려면 더해줘야되는지, 줄여줘야하는지.

    for i in range(n):
        for j in range(m):
            if arr[i][j]>=floor:
                plus_floor+=arr[i][j]-floor #해당 층을 만드려고 더해주는 블록
            else:
                minus_floor+=floor-arr[i][j] #해당 층을 만드려고 빼주는 블록

    if b>=minus_floor-plus_floor:  #주어진 블록이 빼줘야하는 블록 - 더해줘야하는 블록보다 많아야된다.
        #그래야 블록이 남아서 해당 층에 맞게끔 땅 다지기를 할 수 있음.
        if minus_floor+(plus_floor*2)<=answer:
            answer=minus_floor+(plus_floor*2)
            answerFloor=floor
    

print(answer,answerFloor)

