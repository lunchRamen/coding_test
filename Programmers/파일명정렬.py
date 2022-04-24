"""
풀이법

1. HEAD,NUMBER,TAIL을 분리한다.
    - HEAD 분리법 = file[i]가 시작된 부분 전까지.
    - NUMBER분리법 = 이전 글자는 숫잔데, 이후글자는 숫자가 아닌곳
        - 여기서, 숫자길이가 5초과가 되더라도 5까지만 잘라야하기때문에 분기를 따져준다.
        - 그리고 flag란 분기를 둬서, NUMBER와 TAIL이 안 나눠졌다면 그에 대한 NUMBER TAIL처리를 해준다.
2. 나눈 HEAD NUMBER TAIL을 알맞게 정렬한다.
HEAD에 대해선 .lower로 대소문자 맞춰준다음 첫번째 정렬기준
NUMBER에 대해선 int로 씌워서 (lstrip("0))을 하면 런타임 에러가 나던데, 이건 00000이 경우가 있어서 그런듯.

3. 나눈 세 부분을 합쳐서 answer에 추가한다.
"""


def solution(files):
    answer = []
    
    temp=[]
    for file in files:
        t=[]
        for i in range(len(file)):
            idx=0
            if "0"<=file[i]<="9":
                if idx==0:#number부분 첫 시작이라면
                    idx=i
                    t.append(file[:i])  #숫자 전부분까지 자른다.
                    break
        #number,tail부분 찾아내기. 이경우 주의해야할 점은 number로 끝나는 경우에 대한 예외처리를 해줘야함.
        flag=True
        for i in range(idx,len(file)):
            if "0"<=file[i-1]<="9" and (file[i]<"0" or file[i]>"9"):
                if i-idx<=5:
                    t.append(file[idx:i])
                    t.append(file[i:])
                    flag=False
                    break
                else:
                    t.append(file[idx:idx+5])
                    t.append(file[idx+5:])
                    flag=False
                    break
        if flag:    #만약, number와 tail을 분리 못했다면? 숫자로 끝난 것.
            t.append(file[idx:])
            t.append("")
        temp.append(t)
    #일단 head number tail부분 분리 성공.
    temp=sorted(temp,key=lambda x:(x[0].lower(),int(x[1])))
    print(temp)
    for i in range(len(temp)):
        s="".join(temp[i])
        answer.append(s)

    return answer