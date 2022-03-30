"""
그림만 보고 tree문제인줄 앎.
그러나 name:money로 매핑시키면 dict도 가능.
enroll(등록된 판매자 명수) seller(판매한 사람)의 최악을 따져보면,
1억이 넘어서 시간복잡도 초과.

-> amount의 element의 범위가 최대 100인걸 이용, 한번에 최대 얻을수 있는 이익은 10000원
임을 이용해서 한번 타고 올라갈때마다 *0.1씩 하게 되고, 1원미만인 돈은 생각할 필요가 
없으니 depth를 5만 따져주면 되는 문제로 변함. 위의 케이스로 따졌으면 10000*1000000였음.

풀이
일단 enroll에는 root node(민호)가 포함 안되어있고,
answer엔 root node가 제일 첫번째로 포함되어야함을 인지.

그리고 이름-번호의 dict를 하나 생성.
그다음 부모노드를 기억하는 parents배열을 만드는데, 여기서 위에 만들었던
dict의 value와 매핑을 시켜줌.

그다음 d[enroll[i]]=i+1로 부모노드를 제외한 1번노드부터 시작되게끔 적어줌
-> john:1 mary:2 이렇게 d에 저장된다.

그 다음, refarral(추천인)을 통해 부모노드를 설정하는데
referral이 -인 경우=root node가 부모노드니까 제외하고, 나머지 경우라면
parents[i+1]=d[referral[i]]로 1번노드부터 시작하니까 i+1처리를 해준 다음
해당 노드의 부모노드를 d[referral[i]]를 통해 부모노드의 번호를
parents[i+1](i+1번째 노드의 부모노드 "번호"저장)에 저장한다.

그 다음, seller 배열을 타고 판매된 칫솔들에 대한 이익 분배를 진행.
이건 find함수를 따로 만들어서 정의했는데, 여기서 필요한 인자들은
부모노드의 인덱스를 담고 있는 parents 배열
판 칫솔 갯수 *100인 money
자신의 node번호를 가르키는 number(=d[seller[i]])
그 다음 answer배열이다.

이걸 함수로 안빼고 그냥 for문 안에서 처리를 할 수 있음에도 한 이유는
부모노드를 타고 타고 들어가야하기때문에 재귀함수로 처리하는게 가장 적절하기때문.

그래서 재귀의 탈출 조건은
parents[number]==number(이 조건은 부모노드외엔 존재하지않음)
->부모노드에 도착했거나
money//10==0 10을 나눴더니 0이 됐거나
->더이상 돈을 나눠도 0이라 재귀를 탈 이유가 없음.

이러면 answer[number](현재 노드)에 money를 더해주고 return하고
아니라면?
부모노드에 보내줄 돈을 money//10으로 해놓고,
내건 money-send로(90프로) 만든 다음
answer[number] = 내 돈에 mine을 더하고
재귀호출을 하는데 달라진 점은
money부와 number부이다.

왜냐하면 부모노드의 입장에서 재귀를 돌려야하기때문에
부모노드 입장에서 가진 금액은 money//10으로 갱신되어야하고
부모노드 입장에서의 자신의 index는 parents[number]로 자식노드의 value로 들어가면 됨.
"""

def find(parents, money, number, answer):
    # 민호까지 돈이 들어오거나 줄 돈이 없으면 종료
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)  # 총 사람 수(민호 포함 X)
    answer = [0] * (n + 1)  # 민호 포함
    d = {}  # 이름-번호의 key-value를 가지는 딕셔너리
    parents = [i for i in range(n + 1)]  # 각자 자신을 부모로 초기화
    # 이름-번호로 딕셔너리에 저장
    for i in range(n):
        d[enroll[i]] = i + 1
    # 추천인 입력
    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    # 칫솔 정산
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]