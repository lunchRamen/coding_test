import math
"""
for문의 탈출조건
1.전 단어의 마지막 글자로 시작하지 않거나
2.앞에 나왔던 단어를 중복 사용하거나
이거 두개를 분기로 만들고,
1번에 해당하는 마지막글자를 담을 startChar
2번에 앞에 나왔던 단어들을 담을 temp
그리고 탈출시 정답을 구하기위한 idx

idx의 경우 우리가 생각하는 수체계를 위해 +1을 해줌.
그 다음, 몇번째 사람이 떨어졌는지는 나머지로(이건 mod라 순환되기떄문 0에대한 처리를 해줘야한다.)
몇번째 차례에서 떨어졌는지는 몫을 올림해서.(해당 몫으로 나눠 떨어지는거까지가 k번째 차례. 소수점이 나오면 k+1번째 차례이기때문)
"""
def solution(n, words):
    answer = [0,0]

    temp=[words[0]]
    startChar=words[0][-1]
    idx=0
    for i in range(1,len(words)):
        if words[i] in temp:
            idx=i
            break
        if not words[i].startswith(startChar):
            idx=i
            break
        temp.append(words[i])
        startChar=words[i][-1]
        word=words[i]
        
    
    if idx==0:
        pass
    else:
        answer[0]=(idx+1)%n
        if answer[0]==0:
            answer[0]+=n
        answer[1]=math.ceil((idx+1)/n)

    return answer