from itertools import combinations, permutations
import sys

input=sys.stdin.readline

n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]

answer=2000000
for start in combinations(range(0,n),int(n/2)):
    if start[0]!=0:  #절반만 탐색하면 됨.
        break
    ex=[i for i in range(n)]
    link=[i for i in ex if i not in start]
    #스타트팀과 링크팀 분리 성공

    startSum=0
    linkSum=0
    #분리된 스타트 링크 팀의 합계 구함
    #순열이 아니라 조합인 이유는, 내가 애초에 하나의 조합을 구하면
    #해당 역순도 더해줬기 때문. 만약 순열로 할거였으면
    #startSum+=arr[i][j]만 해줬으면 동일한 결과가 나옴.
    print(list(combinations(start,2)),list(permutations(start,2)))
    for i,j in combinations(start,2):
        startSum+=arr[i][j]+arr[j][i]
    for i,j in combinations(link,2):
        linkSum+=arr[i][j]+arr[j][i]
    
    if answer>abs(startSum-linkSum):
        answer=abs(startSum-linkSum)

print(answer)
    
    

