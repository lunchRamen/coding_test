"""
어차피 정할 수 있는 경우의 수가 최대 10이라 팩토리얼 연산을 해도 통과함.
완탐 dfs/bfs 그리디 뭘 쓰든 괜찮다.
여기선 dfs와 bfs 두가지를 살펴 볼 예정.

bfs
->조건은 1.해당과녁을 어피치보다 1발 더 쏜다. 2.해당과녁을 넘어간다.로 볼 수 있다.

q의 구성요소 (i번째 과녁,[과녁들을 맞힌 갯수])
처음에 (0,[0,0,0,0,0,0,0,0,0,0,0])으로 시작.

res배열에 추가할 조건
sum(arrow)==n (화살을 다 쐈을때)

과녁들을 맞힌갯수를 돌면서
info[i]>=arrow[i]이면 어피치 점수추가
info[i]<arrow[i]면 라이언 점수추가.

그래서 라이언이 어피치보다 점수가 큰 경우에 maxGap과 대소비교를 한번 더 해서
maxGap보다도 크다면 res배열을 초기화 시킨다음 arrow배열을 넣어준다.
같다면 알아서 추가가 됨.

그다음 고려해야할 경우가 
1.화살을 더 쐈을때(항상 어피치+1로만 간 경우)
그냥 넘어가면 되고
2.화살을 덜 쐈을때(과녁들을 그냥 넘긴경우)
0점 과녁에 n-sum(temp)를 추가해주고(총 화살갯수-여태까지 쏜 화살갯수로 남은 화살갯수 표현)

나머지는 이제 q를 진행 할 수 있는 경우이기때문에
1.어피치과녁 +1 2.넘김 으로 q에 추가한다

그리고 solution에서 정답을 return 해줄때 고려해줄 경우는
1.라이언이 항상 짐 2.라이언이 이김이고 라이언이 이겼을때
1)한가지 경우로 이김 2)두가지 이상의 경우로 이김.이 있다.
그래서 항상 지는 경우는 answer배열에 bfs의 결과물인 res배열이 없는경우이고
len(answer)==0으로 처리
한가지 경우로 이기면 answer[0]을 return
2가지 이상으로 이기면 answer[-1]을 return하는데 그 이유는
우리가 과녁을 10점->0점으로 옮기면서 조건에 맞아 res에 추가되는 과녁배열은
높은점수 많음 -> 낮은점수 많음 순으로 알아서 정렬되어 저장되기때문에
가장 낮은 점수를 더 많이 맞힌 경우는 res에 마지막으로 저장된 과녁배열이다.
"""
from collections import deque

def bfs(n,info):
    res=[]  #결과를 담을 배열
    q=deque([(0,[0,0,0,0,0,0,0,0,0,0,0])])
    #왼쪽 원소 = focus = 몇번째 과녁에 쏘겠다 (10-focus)로 보면 됨.
    #오른쪽 원소 = arrow = 현재 과녁판 상황
    maxGap=0
    #최대 차
    
    while q:
        focus,arrow=q.popleft() #몇번째 과녁에 쏘는지, 현재 과녁 상황은 어떤지
        
        if sum(arrow)==n:   #종료조건. 화살을 다 쐈을때
            apeach,lion=0,0
            for i in range(11):
                #어피치의 i번째 과녁이 0이고 라이언의 i번째 과녁이 0이 아니라면
                #=둘다 해당 과녁을 맞힌적이 있다면= 과녁을 몇번 맞췄는지 따져야함.
                if not (info[i]==0 and arrow[i]==0):
                    #어피치가 같거나 많이 맞췄다
                    if info[i]>=arrow[i]:
                        apeach+=10-i
                    #라이언이 더 많이
                    else:
                        lion+=10-i
            if apeach<lion: #라이언이 이겼으면
                gap=lion-apeach
                if maxGap>gap:  #갭도 maxGap보다 크다면 갱신해줌.
                    continue
                #같은 경우는 따져주지 않았음. 왜냐하면, 같은경우 가장 낮은 점수를 더 많이 맞힌
                #경우를 return해줘야하기때문에 일단 다 집어넣어야함.
                if maxGap<gap:
                    maxGap=gap
                    res.clear
                res.append(arrow)
        #화살을 더 많이 쏜 경우-> q에 append안시키고 넘김
        elif sum(arrow)>n:
            continue
        #0점 과녁까지 간 경우
        elif focus==10:
            temp=arrow.copy()   #과녁을 카피한 다음
            temp[focus]=n-sum(temp) #마지막 0점 과녁에 다 쏜다.
            q.append((-1,temp))
        #화살도 남고, 과녁도 0점이 아닌경우
        else:
            #해당 과녁(focus)를 어피치보다 1발 더 쏴서 q에 추가시킴 - 경우1
            temp=arrow.copy()
            temp[focus]=info[focus]+1
            q.append((focus+1,temp))
            #해당 과녁을 안쏘고 q에 추가시킴 - 경우2
            temp2=arrow.copy()
            temp2[focus]=0
            q.append((focus+1,temp2))
    return res
            

def solution(n, info):
    answer = bfs(n,info)
    if len(answer)==0:
        return [-1]
    elif len(answer)==1:
        return answer[0]
    else:
        return answer[-1]