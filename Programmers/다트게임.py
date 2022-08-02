def solution(dartResult):
    answer = []
    temp=""
    if "*" in dartResult:
        temp=dartResult.split("*")
    #단순 구현 문제. 다만, 고려해야할 사항이 많음.
    #문자열을 돌면서, S D T인 경우엔 숫자에 대해 제곱해서 answer에 저장.
    #만약 *의 경우, answer에 맨뒤 두개가 있으면 두개를 2배, 한개만 있으면 하나만 2배(try-except로 구현)
    # #의 경우, 마지막을 음수로 바꿈. 그다음 합을 return
    i=0
    while True:
        if i==len(dartResult):
            break
        
        if dartResult[i]=="S" or dartResult[i]=="D" or dartResult[i]=="T":
            num=0
            if dartResult[i-1]=="0":
                try:
                    num=int(dartResult[i-2]+dartResult[i-1])
                except:
                    num=0
            else:
                num=int(dartResult[i-1])
            if dartResult[i]=="S":
                answer.append(num**1)
            elif dartResult[i]=="D":
                answer.append(num**2)
            else:
                answer.append(num**3)
        if dartResult[i]=="*":
            try:
                answer[-2]=answer[-2]*2
                answer[-1]=answer[-1]*2
            except:
                answer[-1]=answer[-1]*2
        
        if dartResult[i]=="#":
            answer[-1]=-answer[-1]
        i+=1
    return sum(answer)
