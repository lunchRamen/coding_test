"""
스킬트리문제에 있어서 가장 중요한점
-> skill문자열의 순서대로 skill_tree문자열이 진행되고있는가.
그리고, 주의해야할 점은
C B는 되지만
B D는 안됨
-> skill의 처음부터 시작하는 부분집합은 되지만
    중간부터 시작하는 부분집합은 X

입력이 다 작아서 팩토리얼만 아니면 다 됨.

skill_tree를 돌면서, skill_tree의 문자가 skill문자열에 있는데
그게 skill의 순서대로 있는가. = idx를 0번부터 설정한 후
맞다면 idx를 1 올리고
틀리다면 skill의 순서와 다르므로 flag를 False로 하고 break하면 됨.
"""


def solution(skill, skill_trees):
    answer = 0
    

    for skill_tree in skill_trees:
        flag=True
        idx=0
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                if skill_tree[i]==skill[idx]:
                    idx+=1
                else:
                    flag=False
                    break
        if flag:
            answer+=1
                
                
    return answer