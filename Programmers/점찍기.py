import math
"""
좌표평면이란게 중요함.
좌표평면에서 거리를 통해 나타낼 수 있는 도형이 원이고, 원은
x**2 + y**2 = d**2라는것을 알면
y의 방정식으로 바꿔서
y = math.sqrt(d**2-x**2)로 해서
0~d+1까지의 y에 대해 몇개의 좌표가 찍히는지 알 수 있다.

"""
def solution(k, d):
    answer=0
    for i in range(0,d+1,k):
        y = math.sqrt(d**2-i**2)
        answer+=math.floor(y/k)+1
    return answer
