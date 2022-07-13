from collections import defaultdict
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    dic=defaultdict(list)
    
    for i in range(len(report)):
        user1,user2=report[i].split()
        dic[user2].append(user1)
    
    for i in range(len(id_list)):
        num=len(set(dic[id_list[i]]))
        tempArr=dic[id_list[i]]
        if num>=k:
            for j in range(len(id_list)):
                if id_list[j] in tempArr:
                    answer[j]+=1
    
        
    return answer