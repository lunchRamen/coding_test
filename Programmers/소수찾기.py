import sys
import itertools

input=sys.stdin.readline

"""
생각 자체는 비슷했다.
다만, 문자열을 다루는 방법에 있어서 순열이나 조합을 따질때는
itertools의 permutations나 combinations를 써서하면 알아서 다 해준다.

우리가 원하는건, numbers문자열에 있는 숫자들을
1자리~ n자리까지 모든 조합을 만든다음, 해당 숫자 조합을 각각 소수 체크해서
소수면 정답 처리를 해주고 싶음.

그래서 solution의 첫번째 for문이 numbers를 1~n개만큼 조합해서 temp에
추가하는 작업.

위처럼 temp작업을 한 후 print해보면 tuple형태로 각 자리수마다의 조합이
tuple형태로 들어가 있음. 이것도 tuple하나를 하나의 원소로 둬서 합칠수 있어서
num배열에 temp의 각 element들을 join시킨다음 int형으로 변환 시킨걸 볼 수 있다.

그 다음 여기에 들어간 num배열들에 대해 소수 판별을 돌리고,
소수판별로 돌린걸 answer배열에 넣는데, 그러면 중복이 생길 수 있음
그래서 set으로 중복제거하고 answer 배열 길이를 return해주는게 답이 된다.


"""

def checkPrime(number):
    if number<2:
        return False
    
    for i in range(2,number):
        if number%i==0:
            return False
    return True
def solution(numbers):
    answer = []
    numbers=list(numbers)
    temp=[]
    
    for i in range(1,len(numbers)+1):
        temp+=set(list(itertools.permutations(numbers,i)))
    num=[int("".join(t)) for t in temp]
    
    for i in num:
        if checkPrime(i):
            answer.append(i)
    
    return len(set(answer))


