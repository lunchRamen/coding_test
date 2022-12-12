def solution(food):
    """
    food에 대해서 순회하면서,
    각 idx를 food[i]//2만큼 추가하고, 다 순회했다면
    0을 추가한 다음 해당 문자열을 거꾸로 뒤집은걸 더해주면 된다.
    """
    answer = ''
    
    for i in range(1,len(food)):
        answer+=str(i)*(food[i]//2)
    temp = answer
    answer+='0'
    answer+=temp[::-1]
    
        
        
    return answer
