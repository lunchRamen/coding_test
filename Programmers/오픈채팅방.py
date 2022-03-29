"""
풀이 방법
일단 uid{number}에 따라 이름이 정해지니까
딕셔너리를 떠올림.
그 다음, 우리가 알면 되는건 Enter 혹은 Change에서 마지막 닉네임만 필요하니까
일단 dic로 userid에 맞는 username을 다 받아놓음 다음, 마지막 username만 새로 dict로 만듬.
그 후, Enter와 Leave에 대해서 newDic[userid](=value값)을 result에 넣어주면 됐다.
"""

import collections
def solution(record):
    result = []
    dic=collections.defaultdict(list)
    for i in range(len(record)):
        temp=list(map(str,record[i].split()))
        
        if temp[0]=="Leave":
            continue
        else:
            if temp[1] in dic:
                dic[temp[1]].append(temp[2])
            else:
                dic[temp[1]]=[temp[2]]
    newDic=dict()
    for i in dic.keys():
        newDic[i]=dic[i][len(dic[i])-1]
    
    for i in range(len(record)):
        temp=list(map(str,record[i].split()))
        if temp[0]=="Enter":
            result.append(f"{newDic[temp[1]]}님이 들어왔습니다.")
        if temp[0]=="Leave":
            result.append(f"{newDic[temp[1]]}님이 나갔습니다.")
        if temp[0]=="Change":
            continue
    return result