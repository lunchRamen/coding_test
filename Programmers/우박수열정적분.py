def solution(k, ranges):
    """
    콜라츠 추측에 의해
    시도횟수를 x축, 시도마다 나온 수를 y축으로 한 그래프를
    정적분했을때 넓이를 구하는 문제.
    각 정적분의 넓이는 1을 기준으로
    (둘 중 큰 y좌표) - abs(y1-y2)*1/2이다.
    직사각형에서 삐져나온 삼각형의 넓이를 뺀 값.
    그리고 [a,b]에 대한걸
    0+a ~ (x+b) 에 대한 범위란걸 인지하고 반복문을 돌리면, 문제가 풀림.
    """
    answer = []
    start = k
    arr = []
    x = 0
    arr.append([x,k])
    while k>1:
        x+=1
        if k%2 == 0:
            k//=2
        elif k%2==1:
            k = (k*3)+1
        if k <= 1:
            break
        arr.append([x,k])
    arr.append([x,k])
    
    dp = [0 for _ in range(len(arr))]
    
    for i in range(1,len(dp)):
        x1,y1 = arr[i-1][0],arr[i-1][1]
        x2,y2 = arr[i][0],arr[i][1]
        
        dp[i] = max(y1,y2) - (abs(y1-y2)*1/2)
    dp[0] = sum(dp)
    
    for x1,x2 in ranges:
        if x1 == 0 and x2 == 0:
            answer.append(dp[0])
            continue
        if x1 > x+x2:
            answer.append(-1)
            continue
        if x1 == x+x2:
            answer.append(0)
            continue
        num = 0
        for i in range(x1,x+x2):
            num+=dp[i+1]
        
        answer.append(num)
            
        
    
    return answer
