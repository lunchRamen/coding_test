"""
정답 코드.(내가 전에 days배열로 배포가능한 기능들은 cpp참고)
days배열로 각 processes[i]를 구현하는데 몇일이 걸리는지 알 수 있다.

예를 들어, days=[5,10,1,1,20,1] 이면
눈으로 봤을땐 5일차때 1개, 10일차때 3개, 20일차때 2개 이렇게 1,3,2지만
이걸 코드로 옮기는게 너무 어려웠다. 그리고 파이썬의 for문은 range(i)를 넣었다면
i의 건너뛰기가 안됨. -> index를 조작하고싶다면 while문으로 구현해야함.

cnt=1로 잡으면, 이미 첫째날을 세었다는 의미니까 i도 1부터 시작을 해야함.
만약 s가 days[i]보다 작으면, -> process s를 배포할때 days[i-1]까지 배포가 가능
-> 그때까지 추가한 cnt를 answer에 넣고, cnt=1로 초기화 한 다음에 s=days[i]로 다시 시작.

만약 s>=days[i]라면, cnt+=1함

그리고 여기가 중요했는데, 만약 i가 days배열의 마지막 원소라면,
그냥 현재 cnt를 넣고 마무리해주면 됨(뒤에 더이상 원소가 없으니까)
"""


def solution(progresses, speeds):
    answer = []
    days=[0]*len(progresses)
    #이게 코드는 훨씬 깔끔함.
    for i in range(len(progresses)):
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            days[i]+=1
    # while True:
    #     flag=True
    #     for i in range(len(progresses)):
    #         if progresses[i]<100:
    #             flag=False
    #     if flag:
    #         break
    #     for i in range(len(progresses)):
    #         progresses[i]+=speeds[i]
    #     day+=1
    #     for i in range(len(progresses)):
    #         if progresses[i]>=100:
    #             if days[i]==0:
    #                 days[i]=day
    #             else:
    #                 continue
    
    i=1
    s=days[0]
    cnt=1
    while i<len(days):
        if s<days[i]:
            answer.append(cnt)
            cnt=1
            s=days[i]
        else:
            cnt+=1
        if i==len(days)-1:
            answer.append(cnt)
        i+=1
    
        
    return answer