"""
처음 생각했던 풀이범
citations배열을 h==h_index가 될때까지 돌려서
같으면 answer=h로 하고 break해서 answer를 return하는 방식인데,
이러면 TC두개가 안뚫림.
아마 len(citations)가 1000에 근접한 경우인가봄.
->아니였음 그냥 특정 조건을 못맞춰줘서 그런가봄.(사실 input=1000이면 2중 for문도 가능.)

->해결 방안
나의 경우 h==h_index:인 경우에만 break를 할 수 있게끔 해줬었다.
그러나, 문제설명을 보면 h번 "이상" 인용이란 문구가 있다.
이건, h>=h_index로 수정해야함을 의미.
(이전의 경우는 h번 이상 인용된 논문이 h편인 경우에만 정답을 구했었음.)
또한, answer에 들어갈 값은 h가 아닌 h_index이다.
우리가 지금 for문을 통해서 돌린건 h_index를 찾으려고 돌린것이기때문.

-> 결론적으로 이 문제에서 요구한것은
citations[i]가 h이상인 것들의 갯수를 구하는 것.
이 갯수는 h_index로 저장해놓기때문에 answer는 h가 아니라 h_index가 되어야함.
->문제의 이상 이하 같을 때나 어떤 변수가 answer에 들어가야하는지 정확히 구분해야겠다.
"""

def solution(citations):
    answer = 0
    
    citations.sort()
    
    h=1
    while True:
        h_index=0
        for i in range(len(citations)):
            if h<=citations[i]:
                h_index+=1

        if h>=h_index:
            answer=h_index
            break
        else:
            h+=1
            
    
    return answer