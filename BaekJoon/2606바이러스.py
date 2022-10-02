n=int(input())

k=int(input())

arr=[[] for _ in range(n+1)]

"""
단순히 그래프에서 노드들을 입력받고,
1번노드와 연결된 노드들의 갯수를 return해주는 문제.
"""

for i in range(k):
    a,b=map(int,input().split(" "))
    arr[a].append(b)
    arr[b].append(a)

answer=0
visit=[False for _ in range(n+1)]
def dfs(idx):
    global answer
    if visit[idx]:
        return
    visit[idx]=True
    answer+=1

    for i in range(len(arr[idx])):
        dfs(arr[idx][i])


dfs(1)
print(answer-1)
