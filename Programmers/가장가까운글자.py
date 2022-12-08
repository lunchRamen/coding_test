from collections import defaultdict
"""
s를 순회하면서, s[i]부터 s[0]까지 거꾸로 순회하며 같은 문자를 찾으면, i-j를 idx로 설정하고 break
만약에 시간복잡도가 N**2 밑이여야한다면,
dic을 만들고, s를 순회하면서, dic[s[i]]에 대해서 dic[s[i]][j] == i에 대해 
dic[s[i]][j-1]를 추가. 근데 이게 시간복잡도가 얼마나 더 낮아질지는 모르겠다.
"""
def solution(s):
    answer = []
    
    for i in range(len(s)):
        idx = -1
        for j in range(i-1,-1,-1):
            if s[i]==s[j]:
                idx = i-j
                break
        answer.append(idx)
    
    
    return answer
