"""
9월 15일 하루치의 로그데이터를 lines로 입력받고,
거기에 맞게끔 초당 최대 처리량을 계산.
->처음 날짜 부분은 필요없음. 응답완료시간,처리시간만 필요.

초로 다 통일시켜주기 위해서 시간부분을 :로 쪼개서 시*3600 분*60 초는 xx.xxx형태니까 float으로
그 다음 밀리세컨 살려주기위해서 소숫점 3번째자리까지 살림. = 응답완료시간을 초로 나타냄(end)

그 다음 lines[idx]를 재정의 할건데 [응답완료시간,응답시작시간]으로 재정의 함.
응답시작시간같은 경우 응답완료시간-처리시간을 해주면 되는데,
처리시간이 x.xxxs가 붙어있어 뒤에 s를 제거해주기 위해서 float(time[1][:-1])로 표현.
그다음, 원래 input의 조건에 맞게 응답완료시간을 기준으로 sort해준다.

이제는 lines에 저장한 원소들이 [응답완료시간,응답시작시간] 형태니까
각 원소들에 대해서 그 원소로부터 0.999초 이내에 몇개나 같은 범위에 걸칠지 조사를 해주면 됨.

-> 그래서 outer loop은 범위가 len(lines)-1이고, inner loop이 len(lines).
temp=1로 걸치는 범위가 몇갠지 일단 자기자신 찍고 시작.

inner loop은 outer loop의 idx+1부터 끝까지 돌려야하니까 lines[idx+1:]로 range를 해줄수있다.
근데 그냥 통일성을 위해 range(idx+1,len(lines))로 수정.
그 다음, 비교 당할 원소의 응답 시작시간([1])이 비교 시작 원소의 완료시간+0.999보다 작다면?
1초 이내에 같이 처리되어야하기때문에 temp+=1를 시켜준다.

그래서 inner loop를 벗어나면 i번째에 대해 i+1~끝까지 1초이내에 몇개나 걸치는지 확인한거니까
temp>answer라면 answer=temp로 갱신시켜줌.

"""


def solution(lines):
    answer = 1
    for idx,time in enumerate(lines):
        time=time.split()[1:]  #날짜는 필요가 없음. [응답요청시간,처리시간] 들어가있음.
        clock=time[0].split(":") #응답완료시간을 :기준으로 다 쪼개줌. 초로 통일시키기 위함.
        end=round(int(clock[0])*3600 + int(clock[1])*60 + float(clock[2]),3)
        #응답완료시간을 시*3600 분*60 초는 밀리세컨도 포함이라 소숫점 3번째 자리까지 표현.
        lines[idx]=[end, end-float(time[1][:-1])]
        #lines를 응답완료시간과 응답시작시간을 넣는데, time[1]의 경우 1.141s처럼
        #뒤에 s가 붙어있는 형태라 뒤에 s를빼주기 위해 [:-1]를 해줌.
    lines.sort(key= lambda x:x[0])
    #응답완료시간을 기준으로 sort해줌 주어진 input과 동일하게 맞춰주기위해.
    
    
    for idx in range(len(lines)-1):
        #idx+1~len(lines)까지 돌릴거라 idx는 len(lines)-1까지 돌려야함.
        temp=1  #동시에 돌아야하는 업무 수 체크 변수
        for nextI in range(idx+1,len(lines)): 
            #idx와 1초이내 같은 처리범위인지 확인할 inner loop
            if lines[idx][0]+0.999>lines[nextI][1]:
                #lines는 [응답완료,응답시작]으로 재정의 했기에,
                #현재 응답완료시간+0.999보다 start의 응답시작시간이 작다면
                #=1초 이내 같이 동작해야할 초당 처리량으로 되기때문에 temp+=1를 해줘야함.
                temp+=1
        if temp>answer:
            answer=temp
        
        
    return answer