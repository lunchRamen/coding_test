"""
예를 들어,
["ba","na","n","a"] "banana"에서

b -> 없음 = len(t)+1이 들어감.
ba -> ba, a
      dp[2-2]+1 , dp[2-1]+1이 들어감.
      이 순간부터 이미 a를 하는건 비교가 안된다.
      왜냐하면, 조합할수 없는 문자열의 경우 이미 맥스값을 넣어놨으니까.
    
ban-> n -> ba + n =2

bana-> na -> ba + na=2
banan -> n -> bana + n = 3
banana -> na -> bana + na =3
그래서 마지막 banana를 3개로 만들수 있어서 3이 나옴.
"""


#ver1
def solution(strs, t):
    n = len(t)
    dp = [0] * (n + 1)
    strs = set(strs)  # set을 사용하면 탐색할 때 시간복잡도 O(1)

    #범위가 0~n이 아니라,1~n+1이다.
    #왜냐하면, t를 슬라이싱할때, i가 마지막에 와야하기때문에
    #파이썬의 문자열,리스트 슬라이싱은 마지막 idx-1이여서 i를 1부터 둔다.
    for i in range(1,n+1):
        dp[i] = len(t)+1  # i번째 시작시 최댓값으로 바꿔줌(최솟값 비교를 위해)
        #strs에 들어있는 문자의 길이는 1~5까지라서.
        for k in range(1,6):
            # 인덱스 범위 때문에..
            #1개~5개를 다 조사할건데, 만약 k가 i보다 크면,
            #인덱스 초과 에러가 뜨니까, s(시작)을 0으로 둠
            if i - k < 0:   
                s = 0
            #아니라면 t의 i번째-k를 문자의 시작으로 둔다.
            else:
                s = i - k
            #그리고 s~i-1까지의 부분문자열이 strs배열에 있는지 검색.
            if t[s:i] in strs:
                #있다면, dp[i]를 현재 값과
                #dp[i-k](t[s:i]를 썼을때, i-k번째까지 사용했던 부분문자열의 갯수 +t[s:i] 1개)
                #를 비교해서 작은 값을 넣어준다. 이건 t의 index가 한칸씩 움직일때마다
                #매번 k를 1~5까지 검색하기때문에 해당 부분문자열의 길이기 1~5까지 중
                #가장 짧은 부분문자열의 합이 dp[i]에 저장되게 된다.
                dp[i] = min(dp[i], dp[i - k] + 1)
    #이렇게 2중 for문을 돌면서 dp[n]엔 t의 길이를 만드는데 필요한
    #strs의 갯수의 최솟값이 들어간다. 만약 이게 len(t)+1이라면 갱신된게
    #없으므로 -1 있다면 그걸 answer에 넣어주면 됨.
    if dp[-1] == len(t)+1:
        answer = -1
    else:
        answer = dp[-1]

    return answer

print(solution(["ba","na","n","a"],"banana"))


#Ver2
# def solution(strs, t):
#     answer = 0
#     strs = set(strs) # 중복제거
#     n = len(t) 
#     dp = [sys.maxsize]*(n+1)
#     dp[0] = 0 # dp의 첫번째 값은 아무 의미없기 때문에 0으로 처리

# 	for i in range(n):
#         s = i
            
#         for j in range(1, 6):
#             e = s + j
#             if e > n:
#                 break
        
#             string = t[s:e]
#             if string in strs:
#                 dp[e] = min(dp[s]+1, dp[e])
                
#     return -1 if dp[-1] == sys.maxsize else dp[-1]