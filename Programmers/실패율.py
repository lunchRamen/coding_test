from collections import defaultdict
def solution(N, stages):
    answer = []
    #실패율 = 스테이지에 도달했으나 클리어 하지 못한 유저 / 스테이지 클리어 + 클리어x
    #스테이지 자체에 아무도 도달 못한경우, zerodivision발생하는것 주의.
    arr=[0 for _ in range(max(max(stages),N)+1)]
    dic=defaultdict(int)
    
    for i in range(1,N+1):
        dic[i]=0
    
    for stage in stages:
        dic[stage]+=1
        for i in range(1,stage+1):
            arr[i]+=1
            
    for i in range(1,N+1):
        if arr[i]==0:
            answer.append(0)
        else:
            answer.append(dic[i]/arr[i])
    
    dic=dict()
    for i in range(len(answer)):
        dic[i+1]=answer[i]
    answer=sorted(dic.items(),key=lambda x:(x[1],-x[0]),reverse=True)
    
    temp=[]
    for i in range(len(answer)):
        temp.append(answer[i][0])
    
    return temp
