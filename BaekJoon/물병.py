import sys

input=sys.stdin.readline

"""
K개를 넘지 않는 비어있지 않은 물병을 만들려고 한다.
->
예를 들어 10병의 물병을 K병을 넘지않는 비어있지 않은 물병을 만든다.

2진수 말곤 시간초과가 난다.

각 물병을 합칠때마다 2의 0승,1승,2승...같이 2의 지수승 형태로 나타남.
그리고 각 병을 합칠때마다
자릿수만 하나씩 올라가지, 1의 갯수는 같다.
ex) 1+1=10(2)
결론적으로, N을 2진수로 나타냈을때 1의갯수가, 필요한 물병의 갯수이다.

-> 1의 갯수(필요한 물병의 갯수)가 K보다 작거나 같을때, 탈출하고
그 전까지 N을 2진수로 나타낸것 중 1이 있는것의 가장 뒤 인덱스부터 가져옴.
그래서, 1과 1을 합쳐서 0으로 만듬.(1의 갯수 줄이기. K가 더 크니까.)
이때 물병의 갯수는 2의 지수승만큼씩 더 필요하고,
N도 2의 지수승씩 더해준다.
"""

N, K = map(int, input().split())

purchased_water_bottle_cnt = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    purchased_water_bottle_cnt += 2**idx
    N += 2**idx

print(purchased_water_bottle_cnt)