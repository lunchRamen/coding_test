import sys

input=sys.stdin.readline

"""
1번부터 n번까지 정답배열(answer)가 주어졌을때,
1,2,3번 중 누가 가장 많은 문제를 맞췄는지 배열에 담아 return해줌.
1번이 찍는 순서: 1,2,3,4,5 반복
2번이 찍는 순서: 2,1 2,3 2,4 2,5 반복
3번이 찍는 순서: 3,3 1,1 2,2, 4,4 5,5 반복.

input=10000
-> 2중 for문까진 괜찮다.

푸는 방법=mod 연산으로 진행.

"""


def solution(answers):
    answer = []
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    
    a,b,c=0,0,0
    
    for i in range(len(answers)):
        if answers[i]==num1[i%5]:
            a+=1
        if answers[i]==num2[i%8]:
            b+=1
        if answers[i]==num3[i%10]:
            c+=1
    maxNum=max(a,b,c)
    
    if a==maxNum:
        answer.append(1)
    if b==maxNum:
        answer.append(2)
    if c==maxNum:
        answer.append(3)
    return answer
