n=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input())))

"""
1이 시작되는 노드부터, 연결된 모든 노드들을 하나의 그룹으로 만든다.
여기서 각 그룹의 갯수를 출력,
이후 각 그룹의 1의 갯수를 출력.

각 그룹의 갯수는 방문 안하고, 1인 것부터 시작될때 +=1을 해주면되는데
각 그룹의 1의 갯수를 구하는게 살짝 헷갈렸다.
결론은, 전역변수를 하나 두고, 위에처럼 그룹 시작될때 0으로 초기화를
해주고 해당 전역변수를 배열에 추가한다.
"""


visit = [[False]*n for _ in range(n)]
cnt=0
count=0

count_arr=[]
c=0
def dfs(i,j):
    global c
    dx= [-1,1,0,0]
    dy=[0,0,1,-1]

    visit[i][j]=1
    c+=1

    for m in range(4):
        nx=i+dx[m]
        ny=j+dy[m]

        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny]==1 and not visit[nx][ny]:
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and not visit[i][j]:
            cnt+=1
            c=0
            dfs(i,j)
            count_arr.append(c)

count_arr.sort()

print(cnt)
for i in count_arr:
    print(i)
