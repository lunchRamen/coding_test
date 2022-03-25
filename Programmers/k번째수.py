"""
2차원 배열에서 for문을 돌릴때 2차원배열의 원소 접근 후 인덱싱 하고싶다면
아래 for문처럼 for command in commands를 하는게 낫다.
for i in range(len(commands))하면 두개 인덱싱해줘야함.(commands[i][0])

그리고 문제에서 준 i번째는 배열의 인덱싱체계가 아니므로 다 -1씩 시켜줘서 구함.
"""
def solution(array, commands):
    answer = []
    
    for command in commands:
        i=command[0]-1
        j=command[1]-1
        k=command[2]-1
        
        temp=array[i:j+1]
        temp=sorted(temp)
        answer.append(temp[k])
    return answer