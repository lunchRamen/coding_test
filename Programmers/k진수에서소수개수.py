import math

"""
3단계로 나눠서 볼 수 있다.
1. 주어진 자연수 N을 K진수로 만드는것
2. K진수로 만든 수를 0으로 나눠서 배열로 만드는 것
(숫자 중간에 0이 들어가면 안되기때문에 그냥 0으로 나누면 된다)
3. 해당 숫자가 1이나 빈문자열이 아니라면, 소수판별을 해서 answer+=1해주는 것.

10진수 숫자가 주어졌을때, K진수를 구하는 법은
해당 숫자의 몫이 0이 될때까지 k로 계속 나눠서 나머지들을 역으로 정렬하면 된다.

그렇게 구한 K진수 수를, 0으로 나눠 list형태로 만든다.
그다음, 해당 숫자들이 "1"이나 빈문자열이 아니라면, int형으로 바꿔 소수판별 한다.
소수라면, answer+=1한다.

**만약, 소수판별을 많이 해야된다면**
에라토스테네스의 체로 input의 최대범위까지 소수판별 배열을 만들고,
해당 인덱스만 불러와서 그게 True,False만 판별해주면 된다.
"""

def get_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
    # x가 해당 수로 나누어 떨어진다면
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    string=""
    while n:
        temp=n%k
        string+=str(temp)
        n=math.trunc(n/k)
    string=string[::-1]
    stringList=string.split("0")
    
    for i in range(len(stringList)):
        temp=stringList[i]
        if temp=="1" or temp=="":
            continue
        else:
            flag=get_prime(int(temp))
            if flag:
                answer+=1
        
    return answer