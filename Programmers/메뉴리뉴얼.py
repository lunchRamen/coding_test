"""
생각 자체는 맞았다.
메뉴의 조합을 key로, 해당 조합이 등장한 횟수를 value로 놓고,
각 코스길이마다 value가 최대인 것을 찾아 return 해주는 방식을 취했다.

그래서 주문들에 대해 주문으로 만들수 있는 코스요리 조합(2가지~len(order)가지)를 구했고
combinations로 만든 list형태는 tuple형태로 만들어져있어 이걸 key로 만들기 위해
문자열 형태로 합치고, dic[temp]가 있으면 value+=1 없으면 value=1로 해서
각 조합에 대한 등장 횟수를 카운팅해줬다.

여기서 유일하게 빼먹은 점이 조합을 할때 sorted(order)를 안해줬다는 점이다.
이게 왜 중요하냐면 TC3에서 나오는데,
XWY와 WXA를 시킨 사람을 봤을때 분명히 XW로 시킨 코스요리가 나와야하는데 나오지 않는다.
왜냐하면, 정렬을 시킨 후 조합을 한다면 조합이 알파벳순으로 나와서 공통된 WX가 나올텐데,
그냥 조합을 했으니 앞에껀 XW 뒤에껀 WX가 나와서 같은 코스요리인데도 카운팅이 되지않음.

그 다음 각 코스요리 길이에 대해 딕셔너리 key들을 사용해서
코스요리길이가 len(key)와 같고 dic[key]가 maxNum보다 크거나 같고 2보다 크다면
maxNum을 갱신시켜준다.

그 후 해당 maxNum과 일치하는 dic[key]를 찾아서 answer에 append시켜주면 정답.
"""
import itertools

def solution(orders, course):
    answer = []
    dic=dict()
    for order in orders:
        length=2
        while length<=len(order):
            nCr=list(itertools.combinations(sorted(order),length))
            for i in nCr:
                temp=''
                for j in i:
                    temp+=j
                if temp in dic:
                    dic[temp]+=1
                else:
                    dic[temp]=1
            length+=1
    #key의 len이 course[i]이고, maxNum을 만들어서 각 courseLen에 맞는 maxNum을 찾음.
    for courseLen in course:
        maxNum=0
        for key in dic.keys():
            if courseLen==len(key):
                if dic[key]>=maxNum and dic[key]>=2:
                    maxNum=dic[key]
        for key in dic.keys():
            if dic[key]==maxNum and len(key)==courseLen:
                answer.append(key)
    answer.sort()
    return answer