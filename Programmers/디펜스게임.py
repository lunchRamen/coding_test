import heapq
"""
라운드가 진행되면서, 무적권을 써야하는 순간마다 i-1라운드까지 중 최대값으로 대체해서 써야한다.
이때 따져줘야하는건
1.무적권이 있는지
2. heapq에 원소가 있는지
3. 있다면, heappop < e인지
를 따져줘서, return해주면 된다.
"""
def solution(n, k, enemy):
    answer = 0
    
    if n>=sum(enemy) or k>=len(enemy):
        return len(enemy)
    
    max_e = []
    for e in enemy:
        flag=True
        if n<e:
            if k>0:
                if max_e:
                    max_num = heapq.heappop(max_e)
                    if max_num[1]<e:
                        heapq.heappush(max_e,(-max_num[1],max_num[1]))
                        n+=e
                        k-=1
                        flag=False
                    else:
                        n+=max_num[1]
                        k-=1
                else:
                    n+=e
                    k-=1
                    flag=False
            else:
                break
        if flag:
            answer+=1
            n-=e
            heapq.heappush(max_e,(-e,e))
        else:
            answer+=1
            n-=e
        
    
    return answer
