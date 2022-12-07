from collections import defaultdict
def solution(s):
    answer = 0
    """
    문자열의 끝까지, dic을 만들어가면서 s[0]과 아닌것의 value가 같을때 문자열 자르기를 한다.
    문자열 끝까지 탐색의 기준은, 문자열 자른적이 없거나, 자르고 난 후에는 빈 문자열이 되면 끝나는걸로 한다.
    나머지는 그냥 딕셔너리로 숫자 세주고, 자르는 것.
    """

    while True:
        x=s[0]

        before=len(s)
        dic=defaultdict(int)
        for i in range(len(s)):
            if s[i]==x:
                dic[x]+=1
            else:
                dic['other']+=1
            if dic[x]==dic['other']:
                answer+=1
                s=s[i+1:]
                break
        after=len(s)
        if before==after or after == 0:
            break
    
    
    if s=='':
        return answer
    else:
        return answer+1
