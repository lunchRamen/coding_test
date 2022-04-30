"""
간단한 중복순열 문제.
AEIOU로 1~5개에 대해 중복순열을 모두 구한 list를
sort하면, 문제에 주어진 정렬기준대로 정렬됨
->파이썬 문자열 정렬기준은, 앞글자부터 비교해서 문자열이 길수록 뒤에있고,
문자열의 길이가 같으면 앞에서부터 비교해서 다른것 기준으로 정렬 됨.

그러므로 정렬한 다음, index+1만 해주면 끝.
"""

from itertools import product
def solution(word):
    answer = 0
    
    dic=[]
    for i in range(1,6):
        dic+=list(map("".join,product("AEIOU",repeat=i)))
    dic.sort()
    answer=dic.index(word)+1
    return answer