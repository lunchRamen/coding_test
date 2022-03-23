"""
경우의 수 따지는걸 너무 어렵게 생각했다.
옷 안입는 경우도 따져줘야 하는걸 알았더라면 접근이 훨씬 쉬웠을 것.

옷 종류에 따른 가짓수+1을 다 곱해주고(+1은 안입은 경우)
다 안입은 상태가 기본이니 -1을 해준걸 return해주면 됨.
"""


def solution(clothes):
    answer = 0
    hash_map={}
    for cloth, type in clothes:
        #옷 종류에 맞는게 있는지 찾아보고 있으면 해당 옷종류 +1
        #없으면 0인데, type이 있다는것 자체가 해당 옷 종류가
        #추가되는거니까 +1씩 해준다.
        hash_map[type]=hash_map.get(type,0)+1
    
    answer=1
    #hashmap의 옷 종류들에 대해서 옷들의 경우의 수를 answer
    #에 곱해줌. 안입고 있는 경우도 더해줘야해서 +1
    for type in hash_map:
        answer*=(hash_map[type]+1)
    #이렇게 되면 다 안입는 경우=기본상태가 되기때문에 answer-1
    #를 해줘야 우리가 원하는 답이 나옴.
    return answer-1