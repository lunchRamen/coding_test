"""
k = 사과가 받을 수 있는 점수의 범위 (1~k)
m = 한 상자에 들어갈 사과의 갯수
score = 각 원소마다 사과의 점수.

한 상자에는 무조건 m개를 담아 판매.
상자에 담긴 사과 중 가장 낮은 점수가, 판매 가격의 기준이 됨 min(socre[i])*m = 한 상자 가격
가능한 많은 사과를 팔았을 떄, 최대 이익을 계산.

일단, 몇 상자를 팔 수 있는지 계산. -> len(score)//m.
그 다음, score를 정렬 한 다음 뒤에서부터 탐색해서 (m개씩) 거기서 min씩 쳐내면 될듯.

m개씩 박스의 갯수만큼만 진행시키면 된다.
"""
def solution(k, m, score):
    answer = 0
    
    boxes = len(score)//m
    
    score.sort(reverse=True)
    start = 0
    for i in range(boxes):
        box = score[start:start+m]
        answer+=min(box)*m
        start+=m
    return answer
