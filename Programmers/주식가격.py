"""
해당 문제는 한 배열을 두고 subproblem문제로 풀어야 한다고 생각.
2중 for문을 통해 prices[i]와 prices[i+1:]를 비교한다.
만약 prices[i]<=prices[j]라면, 더 탐색해봐야하니 cnt만 1 추가해주고
prices[i]>prices[j]라면 여기서 주가가 떨어졌다는거니까 똑같이 cnt를 1 추가해주고
"break"한다.
그 다음, prices[i+1:]를 통과한 cnt는 i번째 주식가격이 얼만큼 유지됐는지를 나타내주기때문에
answer.append(cnt)한다.
끝.
"""

def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                cnt+=1
            else:
                cnt+=1
                break
        answer.append(cnt)
    return answer