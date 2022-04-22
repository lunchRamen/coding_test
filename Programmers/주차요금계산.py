from collections import defaultdict

"""
일단, dic으로 차량번호에 맞는 입차,출차시간을 저장한다.
dic을 다 만든 후, dic[key]의 길이가 홀수이면 출차가 없다는 뜻이므로
1439(23:59)를 넣어준다.

그 다음, dic[key]를 순회하면서 총 주차한 시간을 구한다.
주차한 시간에 맞게끔 기본요금과 단위요금을 구한다.
해당 총 주차요금을 dic[key]에 추가한다.

dic.keys()를 정렬한 배열을 만든 다음, 그 배열을 순회하면서
dic[i][-1]를 answer에 추가한다.
"""
def solution(fees, records):
    answer = []
    dic=defaultdict(list)
    
    for i in range(len(records)):
        time,carNum,inOut=records[i].split(" ")
        timeHour,timeMinute=time.split(":")
        time=int(timeHour)*60+int(timeMinute)
        if inOut=="IN":
            dic[carNum].append(time)
            for j in range(i+1,len(records)):
                tempTime,tempCarNum,tempInOut=records[j].split(" ")
                if carNum==tempCarNum and tempInOut=="OUT":
                    tempTimeHour,tempTimeMinute=tempTime.split(":")
                    tempTime=int(tempTimeHour)*60+int(tempTimeMinute)
                    dic[carNum].append(tempTime)
                    break
        else: #inOut이 OUT인 경우 이미 위 for문에서 따져줬음
            continue
    
    for i in dic.keys():
        if len(dic[i])%2 ==0:
            continue
        else:
            dic[i].append(1439)
    
    for carNum in dic.keys():
        totalTime=0
        for i in range(0,len(dic[carNum]),2):
            inTime,outTime=dic[carNum][i],dic[carNum][i+1]
            totalTime+=outTime-inTime
        totalFee=0
        totalFee+=fees[1]
        totalTime-=fees[0]
        
        partialTime=0
        partialFee=fees[3]
        while True:
            if partialTime>=totalTime:
                break
            partialTime+=fees[2]
        totalFee+=int(partialTime/fees[2])*partialFee
        dic[carNum].append(totalFee)
    
    carNumList=list(dic.keys())
    carNumList.sort()
    
    for carNum in carNumList:
        answer.append(dic[carNum][-1])
        
    
    return answer