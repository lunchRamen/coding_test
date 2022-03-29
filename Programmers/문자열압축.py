def solution(s): 
    result=[]
    #주어진 문자열이 1이면 그냥 1. 
    if len(s)==1: 
        return 1
    #1부터 주어진 문자열/2의 몫+1까지. (왜 n까지가 아니고 몫+1까지?)
    #아무 규칙이 없는건 그거 그대로니까. 최대 크기로 쪼갤 수 있는게 문자열 길이/2인데, 홀수일 경우도 마찬가진데,
    #파이썬 for loop index체계때문에 +1해줌(우린 len(s)//2까지 확인해보고 싶은거니까)
    for i in range(1, (len(s)//2)+1):
        b = ''  #문자열 s를 i개씩 쪼갰을때 나오는 결과 문자열.
        cnt = 1 #반복되는 문자열 갯수 체크
        tmp=s[:i]   #체크할 문자열을 temp에 저장. 기본적으로 i개만큼 자르고, 다음 for loop에서 tmp와 비교.
        for j in range(i, len(s), i): #s의 문자열 반복 체크를 위한 for문. 그래서 step이 i개씩.
            if tmp==s[j:i+j]: #만약 체크할 문자열과 j~i+j-1이 같으면
                cnt+=1 #반복횟수 1추가
            else: #같지 않으면
                if cnt!=1: #반복횟수가 1이 아닌경우면
                    b = b + str(cnt)+tmp #반복횟수+ 반복한 문자열을
                else: #1이면 
                    b = b + tmp #그냥 더함 
                tmp=s[j:j+i] # 문자열 s를 다 돌때까지 할거니까 tmp를 다시 초기화 해줌
                cnt = 1 #반복횟수도.
        if cnt!=1: #마지막 tmp에 담겼던 문자열을 처리해주기 위해.
            b = b + str(cnt) + tmp 
        else: b = b + tmp 
        result.append(len(b)) 
    return min(result)