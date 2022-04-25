"""
비록 2시간 걸렸지만, 근성있게 풀어냈다.
일단 시작시간,끝나는시간,노래제목,음표들을 infoList에 2차원배열형태로 담아낸다.

그 다음, 내가 "#"를 처리한 방법은, 일단 음표에 해당하는 문자열을 list로 만든 다음
#인 경우, 이전 원소에 #를 더해주는 작업을 한 후, #만있는 원소를 다 지워낸다.
그렇게 음표들이 담긴 배열을 만들어냄.

그다음 시작시간,끝나는시간을 시,분에 맞게 숫자로 나타내서 playTime을 만든 후, info에 추가한다
왜냐하면, 해당 인수로 조건이 일치하는 음악에서 재생시간을 기준으로 정렬해서 answerList[0]을 반환하려고.
파이썬의 sort알고리즘은 stable하기때문에, 재생시간이 같을 경우 먼저 append된 순서를 보장해준다.
고로, 두번째 경우는 고려해줄 필요가 없다.

또한 구한 playTime만큼의 멜로디 길이를 구해준다(tempMelody)
그 다음, tempMelody와 m을 비교해주는데,
m또한 위의 로직을 기반으로 배열화 시킨다음,
0~배열 끝까지 tempMelody를 len(m)씩 잘랐을때 같은지 확인해서
같다면 answerList에 추가한다.

이렇게 추가한 answerList는 길이가 0이면 None 1이면 answerList[0][2]
2이상이면, sort를 playTime의 오름차순으로 한번 해준다음, answerList[0][2]를 해준다.
"""

def solution(m, musicinfos):
    answer = ''
    answerList=[]
    infoList=[]
    
    for info in musicinfos:
        t=list(map(str,info.split(",")))
        infoList.append(t)
        
    m=list(m)
    for i in range(len(m)):
        if m[i]=="#":
            m[i-1]+="#"
    while "#" in m:
        m.remove("#")
    
    for info in infoList:
        melodyList=list(info[3])
        for i in range(len(melodyList)):
            if melodyList[i]=="#":
                melodyList[i-1]+="#"
        
        while "#" in melodyList:
            melodyList.remove("#")
        #악보를 음에 따라 리스트 원소로 분리.
        #이제 이걸 시작,종료시간에 맞게끔 반복시켜서 infoList[3]을 재정의한다.
        
        startHour,startMinute=info[0].split(":")
        endHour,endMinute=info[1].split(":")
        startMinute=int(startHour)*60+int(startMinute)
        endMinute=int(endHour)*60+int(endMinute)
        
        playTime=endMinute-startMinute
        info.append(playTime)
        repeat=0
        tempMelody=[]
        while True:
            if repeat==0 and len(melodyList)>playTime:
                tempMelody=melodyList[:playTime]
                break
            if playTime<=0:
                break
            tempMelody+=melodyList
            playTime-=len(melodyList)
            repeat+=1
        for i in range(len(tempMelody)):
            if i+len(m)==len(tempMelody)+1:
                break
            if m==tempMelody[i:i+len(m)]:
                answerList.append(info)
                break
    if len(answerList)==0:
        answer="(None)"
    elif len(answerList)==1:
        answer=answerList[0][2]
    else:
        answerList.sort(key=lambda x:x[4],reverse=True)
        answer=answerList[0][2]
            
            
            
    
    return answer


solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])