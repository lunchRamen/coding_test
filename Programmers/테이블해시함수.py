"""
일단, data정렬을 주어진 조건을 만족시키도록 하고,
row_begin ~row_end까지 각 원소를 i로 mod연산한 값들을 저장하는 배열 생성.
그 다음, answer와 하나씩 xor연산을 하여 정답 return

-> 사람의 수체계와 배열의 인덱스체계가 다르고 이걸 일일히 구별해주는것만 잘하면 됨.
"""
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col-1],-x[0]))
    s=[]
    for i in range(row_begin-1, row_end):
        temp = 0
        for j in range(len(data[i])):
            temp+=(data[i][j]%(i+1))
        s.append(temp)
        
    for i in range(len(s)):
        answer = bin(answer ^ s[i])
        answer = int(answer,2)
    return answer
